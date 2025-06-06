# Análise Exploratória de Dados do Perfil de Vento

## Visão Geral

Este projeto apresenta uma análise exploratória detalhada de dados de perfil de vento coletados em diferentes alturas. A análise visa entender padrões, comportamentos e características dos dados de vento, incluindo velocidade, direção e cisalhamento em várias altitudes.

O objetivo principal desta EDA é analisar o perfil de vento e criar um dataset de treinamento com as melhores features para predição da velocidade do vento. O resultado deste processo é o arquivo `processed_variables_engineered.csv`, que contém as variáveis mais relevantes identificadas durante a análise para uso em modelos preditivos.

## Estrutura do Projeto

```
WindProfile_EDA/
│
├── data/                 # Dados brutos e processados
│   └── dataset.csv       # Dataset principal
│
├── notebooks/            # Jupyter notebooks com análises
│   ├── 1_EDA_Overview.ipynb             # Visão geral dos dados
│   ├── 2_Wind_Speed_Analysis.ipynb      # Análise detalhada da velocidade do vento
│   ├── 3_Wind_Direction_Analysis.ipynb  # Análise da direção do vento
│   └── 4_Wavelet_Overview.ipynb         # Análise utilizando dados filtrados pela Wavelet
│
├── images/               # Gráficos e visualizações geradas
│
├── src/                  # Códigos fonte e utilitários
│   └── utils.py          # Funções utilitárias para análise
│
└── docs/                 # Documentação adicional
    └── data_dictionary.md # Dicionário de dados explicando as variáveis
```

## Requisitos

Para executar os notebooks e scripts deste projeto, você precisará das seguintes dependências:

- Python 3.8+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- SQLAlchemy (para operações com banco de dados)
- Wavelet
- Xgboost

Você pode instalar todas as dependências usando:

```bash
pip install -r requirements.txt
```

## Conjunto de Dados

O conjunto de dados contém medições de:
- Velocidade do vento em diferentes alturas (40m-260m)
- Direção do vento em diferentes alturas
- Componentes verticais do vento
- Medidas de cisalhamento
- Dados atmosféricos como temperatura, pressão e umidade

## Análises Principais

1. **Distribuição da Velocidade do Vento**: Análise estatística detalhada das velocidades do vento em diferentes alturas.
2. **Perfis de Vento**: Caracterização dos perfis verticais de vento.
3. **Correlação entre Variáveis**: Identificação de relações entre variáveis como velocidade, direção e cisalhamento.
4. **Análise Temporal**: Identificação de padrões temporais nas medições de vento.
5. **Análise de Direção**: Estudo da variabilidade direcional do vento em diferentes alturas.
6. **Análise dos Dados Filtrados Por Wavelet**: Análise de todas as variáveis filtradas e criação de um dataset otimizado para treinamento e validação de modelos preditivos.

### Uso de Transformadas Wavelet

Um destaque deste projeto é a aplicação de transformadas wavelet para filtrar os dados de vento. Esta técnica de processamento de sinais foi implementada para:

- Remover ruídos de alta frequência dos dados, destacando tendências subjacentes
- Melhorar a qualidade das features utilizadas para modelagem preditiva
- Facilitar o treinamento de modelos, permitindo que aprendam padrões mais consistentes
- Aumentar a precisão nas previsões da velocidade do vento

A filtragem wavelet foi fundamental para criar o dataset `processed_variables_engineered.csv`, que contém as variáveis mais relevantes já pré-processadas para uso em modelos preditivos de velocidade do vento.

## Como Usar

1. Clone este repositório
2. Instale as dependências listadas em `requirements.txt`:
   ```bash
   ./setup.sh
   ```
3. Execute os notebooks individualmente ou use o script para executar todos:
   ```bash
   ./run_notebooks.sh
   ```
   
Os notebooks são convertidos automaticamente do formato VS Code para o formato Jupyter padrão antes da execução. Os notebooks gerados com resultados serão salvos na pasta `notebooks/output/`.

Alternativamente, você pode abrir os notebooks convertidos diretamente na pasta `notebooks/jupyter/` para edição e execução manual.

## Documentação

- [Resumo Executivo](docs/executive_summary.md) (também disponível em português: [Resumo Executivo PT-BR](docs/resumo_executivo.md)) - Principais conclusões e descobertas da análise
- [Dicionário de Dados](docs/data_dictionary.md) - Descrição detalhada de todas as variáveis do conjunto de dados
- [Relatório de Conclusão do Projeto](docs/completion_report.md) (também disponível em português: [Relatório de Conclusão PT-BR](docs/relatorio_conclusao.md)) - Descrição das etapas concluídas e status do projeto

## Resultados

Os principais resultados desta análise incluem:
- Caracterização completa do comportamento do vento em diferentes alturas
- Identificação de padrões de cisalhamento vertical
- Correlação entre variáveis meteorológicas e comportamento do vento
- Geração do dataset `processed_variables_engineered.csv` com as melhores features selecionadas e filtradas para treinamento de modelos preditivos baseados na arquitetura seq2seq
- Seleção otimizada de variáveis através de análise XGBoost e técnicas de processamento de sinais wavelet

## Autor

Lucas Batista Pereira

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
