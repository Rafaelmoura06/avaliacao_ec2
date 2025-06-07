# Streamlit App com 3 Gráficos

Este projeto é um app Streamlit que exibe três gráficos simples usando dados de um arquivo CSV e dados fictícios:

- Gráfico 1: Gráfico de barras da segunda coluna do CSV (se existir).
- Gráfico 2: Histograma da primeira coluna numérica do CSV (se existir).
- Gráfico 3: Gráfico de pizza com dados fictícios.

---

## Pré-requisitos

- Python 3.7 ou superior instalado.
- Pip instalado.
- Acesso à internet para instalar pacotes.

---

 Instalação

1. Clone ou baixe este repositório.

2. Instale as bibliotecas necessárias:

Coloque o arquivo MS_Financial Sample.csv na mesma pasta do script app.py.

Como rodar
No terminal, dentro da pasta do projeto, execute:

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

--server.port 8501 define a porta para acesso (padrão do Streamlit).

--server.address 0.0.0.0 permite acesso remoto (útil para servidores EC2).

Arquivo CSV
O arquivo CSV deve estar separado por ponto e vírgula ; (formato padrão de Excel em português).

Se seu CSV usar outro separador, ajuste o parâmetro sep no pd.read_csv() no código.

Estrutura do código
O app carrega o CSV.

Exibe gráficos baseados nos dados do CSV.

Exibe também um gráfico de pizza com dados fixos.

Observações
Caso seu CSV tenha menos de 2 colunas, o gráfico 1 não será exibido.

Caso seu CSV não tenha colunas numéricas, os gráficos 2 e 3 baseados em CSV não serão exibidos.

O gráfico de pizza é sempre exibido com dados fixos.
