# Dicionário de Dados - Perfil de Vento

Este documento descreve as variáveis presentes no conjunto de dados do perfil de vento.

## Informações Temporais

| Variável | Descrição |
|----------|-----------|
| `id`     | Timestamp no formato YYYY-MM-DD HH:MM:SS |
| `year`   | Ano da medição |
| `month`  | Mês da medição (1-12) |
| `day`    | Dia da medição (1-31) |
| `hour`   | Hora da medição (0-23) |
| `minute` | Minuto da medição (0-59) |

## Variáveis Meteorológicas

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `press`  | Pressão atmosférica | hPa |
| `humid`  | Umidade relativa do ar | % |
| `temp`   | Temperatura | °C |

## Velocidade do Vento (Wind Speed)

As variáveis `ws` seguidas por um número representam a velocidade do vento horizontal na altura indicada pelo número.

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `ws40`   | Velocidade do vento a 40 metros de altura | m/s |
| `ws50`   | Velocidade do vento a 50 metros de altura | m/s |
| ...      | ... | ... |
| `ws260`  | Velocidade do vento a 260 metros de altura | m/s |

## Componentes Verticais do Vento

As variáveis `verts` seguidas por um número representam a componente vertical do vento na altura indicada.

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `verts40`  | Componente vertical do vento a 40 metros de altura | m/s |
| `verts50`  | Componente vertical do vento a 50 metros de altura | m/s |
| ...      | ... | ... |
| `verts260` | Componente vertical do vento a 260 metros de altura | m/s |

## Direção do Vento 

As variáveis `wdir` seguidas por um número representam a direção do vento na altura indicada.

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `wdir40`  | Direção do vento a 40 metros de altura | graus |
| `wdir50`  | Direção do vento a 50 metros de altura | graus |
| ...      | ... | ... |
| `wdir260` | Direção do vento a 260 metros de altura | graus |

## Cisalhamento do Vento

As variáveis `cis` representam o cisalhamento do vento entre diferentes camadas. 

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `cis1`   | Cisalhamento do vento entre as camadas 1 | 1/s |
| `cis2`   | Cisalhamento do vento entre as camadas 2 | 1/s |
| ...      | ... | ... |
| `cis19`  | Cisalhamento do vento entre as camadas 19 | 1/s |

## Dispersão da Velocidade do Vento

As variáveis `wdisp` seguidas por um número representam a dispersão da velocidade do vento na altura indicada.

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `wdisp40`  | Dispersão da velocidade do vento a 40 metros de altura | m/s |
| `wdisp50`  | Dispersão da velocidade do vento a 50 metros de altura | m/s |
| ...      | ... | ... |
| `wdisp260` | Dispersão da velocidade do vento a 260 metros de altura | m/s |

## Dispersão Vertical

As variáveis `vertdisp` seguidas por um número representam a dispersão do componente vertical do vento na altura indicada.

| Variável | Descrição | Unidade |
|----------|-----------|---------|
| `vertdisp40`  | Dispersão da componente vertical a 40 metros de altura | m/s |
| `vertdisp50`  | Dispersão da componente vertical a 50 metros de altura | m/s |
| ...      | ... | ... |
| `vertdisp260` | Dispersão da componente vertical a 260 metros de altura | m/s |
