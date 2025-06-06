"""
Utilitários para análise exploratória de dados do perfil de vento.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from matplotlib.colors import LinearSegmentedColormap
from typing import List, Dict, Tuple, Optional, Union
import warnings
from scipy import stats
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# Configuração de estilo para visualizações
def set_plotting_style():
    """
    Configura o estilo de visualização para gráficos consistentes.
    """
    sns.set_theme(style='whitegrid')
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 12
    
    # Cores personalizadas
    colors = ["#1E88E5", "#FFC107", "#D81B60", "#8D6E63", "#5E35B1", "#00ACC1", "#43A047"]
    sns.set_palette(sns.color_palette(colors))
    
    return colors

def load_wind_data(file_path: str) -> pd.DataFrame:
    """
    Carrega os dados do perfil de vento e realiza pré-processamento básico.
    
    Args:
        file_path: Caminho para o arquivo CSV de dados
        
    Returns:
        DataFrame com os dados carregados e pré-processados
    """
    # Carregar dados
    df = pd.read_csv(file_path)
    
    # Processar o campo id para extrair datetime
    # Primeiro, converte para string e separa a parte antes do ponto (removendo frações de segundo)
    df['id_str'] = df['id'].astype(str).apply(lambda x: x.split('.')[0])
    # Converte para datetime
    df['id_datetime'] = pd.to_datetime(df['id_str'], errors='coerce')
    # Configura o datetime como índice
    df.set_index('id_datetime', inplace=True)
    # Remove a coluna intermediária
    df.drop(columns=['id_str'], inplace=True)
    
    # Verificar dados ausentes
    missing_data = df.isnull().sum()
    if missing_data.sum() > 0:
        print(f"Dados ausentes encontrados:\n{missing_data[missing_data > 0]}")
        # Opção para lidar com valores ausentes (pode ser ajustada conforme necessidade)
        df = df.interpolate(method='time')
    
    # Adicionar colunas adicionais úteis para análise
    df['hour_of_day'] = df.index.hour
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['day'] = df.index.day
    df['year'] = df.index.year
    
    return df

def get_height_columns(df: pd.DataFrame, prefix: str) -> List[str]:
    """
    Extrai as colunas que correspondem a uma determinada variável em diferentes alturas.
    
    Args:
        df: DataFrame com os dados
        prefix: Prefixo das colunas (ex: 'ws', 'wdir', 'verts')
        
    Returns:
        Lista de nomes de colunas ordenadas por altura
    """
    cols = [col for col in df.columns if col.startswith(prefix)]
    # Extrair a altura de cada coluna e ordenar
    heights = [int(col.replace(prefix, '')) for col in cols]
    sorted_cols = [x for _, x in sorted(zip(heights, cols))]
    return sorted_cols

def extract_heights(columns: List[str], prefix: str) -> List[int]:
    """
    Extrai os valores de altura de uma lista de nomes de colunas.
    
    Args:
        columns: Lista de nomes de colunas
        prefix: Prefixo a ser removido para extrair a altura
        
    Returns:
        Lista de alturas como inteiros
    """
    heights = [int(col.replace(prefix, '')) for col in columns]
    return sorted(heights)

def plot_vertical_profile(df: pd.DataFrame, timestamp, variable_prefix: str, 
                          title: str, xlabel: str, add_stats: bool = False,
                          ax=None, color=None):
    """
    Plota o perfil vertical de uma variável para um timestamp específico.
    
    Args:
        df: DataFrame com os dados
        timestamp: Timestamp para o qual plotar o perfil
        variable_prefix: Prefixo das colunas a serem plotadas
        title: Título do gráfico
        xlabel: Etiqueta do eixo x
        add_stats: Se True, adiciona estatísticas ao gráfico
        ax: Eixo matplotlib opcional para o plot
        color: Cor opcional para a linha
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 10))
        
    columns = get_height_columns(df, variable_prefix)
    heights = extract_heights(columns, variable_prefix)
    
    # Obter valores para o timestamp específico
    if timestamp in df.index:
        values = df.loc[timestamp, columns].values
        
        # Plotar o perfil vertical
        if color:
            ax.plot(values, heights, marker='o', linestyle='-', linewidth=2, markersize=6, color=color)
        else:
            ax.plot(values, heights, marker='o', linestyle='-', linewidth=2, markersize=6)
            
        ax.set_title(f"{title} em {timestamp}", fontsize=14)
        ax.set_ylabel("Altura (m)", fontsize=12)
        ax.set_xlabel(xlabel, fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        if add_stats:
            mean = np.mean(values)
            std = np.std(values)
            min_val = np.min(values)
            max_val = np.max(values)
            
            stats_text = f"Média: {mean:.2f}\nDesvio Padrão: {std:.2f}\nMín: {min_val:.2f}\nMáx: {max_val:.2f}"
            ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        return ax
    else:
        warnings.warn(f"Timestamp {timestamp} não encontrado no DataFrame.")
        return ax

def plot_time_series(df: pd.DataFrame, column: str, title: str = None, 
                     ylabel: str = None, resample: str = None, 
                     plot_type: str = 'line', ax=None):
    """
    Plota uma série temporal para uma coluna específica.
    
    Args:
        df: DataFrame com os dados
        column: Coluna a ser plotada
        title: Título do gráfico (opcional)
        ylabel: Etiqueta do eixo y (opcional)
        resample: Regra de reamostragem (ex: 'H' para hora, 'D' para dia)
        plot_type: Tipo de plot ('line', 'scatter', ou 'box')
        ax: Eixo matplotlib opcional para o plot
        
    Returns:
        Eixo matplotlib com o plot
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(14, 6))
        
    data = df[column] if resample is None else df[column].resample(resample).mean()
    
    if plot_type == 'line':
        ax.plot(data.index, data.values, linewidth=2)
    elif plot_type == 'scatter':
        ax.scatter(data.index, data.values, alpha=0.6)
    elif plot_type == 'box':
        if resample is None:
            raise ValueError("Para boxplot, é necessário especificar resample")
        df_resampled = df.resample(resample).agg({column: list})
        box_data = [x for x in df_resampled[column] if len(x) > 0]
        ax.boxplot(box_data)
        ax.set_xticklabels([pd.to_datetime(d).strftime('%Y-%m-%d') for d in df_resampled.index])
        ax.tick_params(axis='x', rotation=45)
        
    if title:
        ax.set_title(title, fontsize=14)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12)
    
    ax.set_xlabel("Data", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Formatação de data no eixo x
    if plot_type != 'box':
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)
    
    return ax

def plot_wind_rose(df: pd.DataFrame, ws_col: str, wdir_col: str, 
                   title: str = None, bins_ws: int = 5, bins_dir: int = 16, ax=None):
    """
    Plota uma rosa dos ventos para visualizar distribuição de direção e velocidade.
    
    Args:
        df: DataFrame com os dados
        ws_col: Coluna de velocidade do vento
        wdir_col: Coluna de direção do vento
        title: Título do gráfico
        bins_ws: Número de bins para velocidade
        bins_dir: Número de bins para direção
        ax: Eixo matplotlib opcional para o plot
        
    Returns:
        Eixo matplotlib com a rosa dos ventos
    """
    from windrose import WindroseAxes
    
    if ax is None:
        fig = plt.figure(figsize=(10, 10))
        rect = [0.1, 0.1, 0.8, 0.8]
        ax = WindroseAxes(fig, rect)
        fig.add_axes(ax)
    
    # Remover valores NaN
    mask = ~(df[ws_col].isna() | df[wdir_col].isna())
    ws_data = df.loc[mask, ws_col]
    wdir_data = df.loc[mask, wdir_col]
    
    # Plotar rosa dos ventos
    ax.bar(wdir_data, ws_data, normed=True, opening=0.8, 
           edgecolor='white', bins=bins_ws, nsector=bins_dir)
    
    # Adicionar legenda e título
    ax.set_legend(title="Velocidade do Vento (m/s)")
    if title:
        ax.set_title(title, fontsize=14)
    
    return ax

def plot_heatmap_by_height_time(df: pd.DataFrame, variable_prefix: str, 
                               title: str, cmap: str = 'viridis', 
                               resample: str = 'D', ax=None):
    """
    Plota um mapa de calor de uma variável por altura e tempo.
    
    Args:
        df: DataFrame com os dados
        variable_prefix: Prefixo das colunas a serem plotadas
        title: Título do gráfico
        cmap: Colormap para o mapa de calor
        resample: Regra de reamostragem (ex: 'D' para dia)
        ax: Eixo matplotlib opcional para o plot
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(14, 8))
    
    columns = get_height_columns(df, variable_prefix)
    heights = extract_heights(columns, variable_prefix)
    
    # Reamostrar dados para reduzir a dimensionalidade temporal
    df_resampled = df[columns].resample(resample).mean()
    
    # Preparar dados para o mapa de calor
    data = df_resampled.T.values
    
    # Plotar mapa de calor
    im = ax.imshow(data, aspect='auto', cmap=cmap, origin='lower', 
                   extent=[0, len(df_resampled), heights[0], heights[-1]])
    
    # Configurar ticks e labels
    num_time_ticks = min(10, len(df_resampled))
    time_indices = np.linspace(0, len(df_resampled) - 1, num_time_ticks, dtype=int)
    ax.set_xticks(time_indices)
    ax.set_xticklabels([df_resampled.index[i].strftime('%Y-%m-%d') for i in time_indices], rotation=45)
    
    # Configurar labels e título
    ax.set_ylabel("Altura (m)", fontsize=12)
    ax.set_xlabel("Data", fontsize=12)
    ax.set_title(title, fontsize=14)
    
    # Adicionar barra de cores
    plt.colorbar(im, ax=ax)
    
    return ax

def create_database_connection(db_name: str = 'DataSet-PerfilVento',
                              user: str = 'root',
                              password: str = 'root',
                              host: str = 'localhost',
                              port: str = '5432'):
    """
    Cria uma conexão com o banco de dados PostgreSQL.
    
    Args:
        db_name: Nome do banco de dados
        user: Nome de usuário
        password: Senha
        host: Host do banco de dados
        port: Porta do banco de dados
        
    Returns:
        Engine do SQLAlchemy para conexão com o banco de dados
    """
    # Configurar string de conexão
    db_url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    
    # Verificar se o banco de dados existe e criar se não existir
    if not database_exists(db_url):
        create_database(db_url)
        print(f"Banco de dados '{db_name}' criado com sucesso.")
    else:
        print(f"Banco de dados '{db_name}' já existe.")
    
    # Criar engine
    engine = create_engine(db_url)
    
    return engine

def windspeed_profile_law(height, reference_height, reference_speed, alpha=0.143):
    """
    Calcula o perfil de velocidade do vento usando a lei de potência.
    
    Args:
        height: Altura para calcular a velocidade
        reference_height: Altura de referência
        reference_speed: Velocidade na altura de referência
        alpha: Expoente da lei de potência (padrão é 0.143 para terreno aberto)
        
    Returns:
        Velocidade estimada na altura especificada
    """
    return reference_speed * (height / reference_height) ** alpha

def calculate_wind_shear_exponent(heights, speeds):
    """
    Calcula o expoente de cisalhamento do vento a partir das velocidades e alturas.
    
    Args:
        heights: Lista de alturas
        speeds: Lista de velocidades correspondentes
        
    Returns:
        Expoente de cisalhamento do vento
    """
    log_heights = np.log(heights)
    log_speeds = np.log(speeds)
    
    # Regressão linear no espaço log-log
    slope, _, r_value, _, _ = stats.linregress(log_heights, log_speeds)
    
    return slope, r_value**2  # Retorna o expoente e o R²
