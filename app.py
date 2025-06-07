
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Streamlit App com 3 Gráficos")
st.subheader("Carregando e visualizando o CSV")


try:
    df = pd.read_csv("MS_Financial Sample.csv", sep=";", on_bad_lines='skip')
    st.success("✅ Arquivo carregado com sucesso!")
except Exception as e:
    st.error(f"❌ Erro ao carregar o CSV: {e}")
    st.stop()

# Gráfico 1: Barras da 2ª coluna (se existir)
if len(df.columns) > 1:
    st.write("### 📊 Gráfico 1: Contagem de valores na segunda coluna")
    fig1, ax1 = plt.subplots()
    df[df.columns[1]].value_counts().plot(kind='bar', ax=ax1, color='lightblue', edgecolor='black')
    ax1.set_xlabel(df.columns[1])
    ax1.set_ylabel("Frequência")
    st.pyplot(fig1)
else:
    st.warning("⚠️ O arquivo tem menos de 2 colunas. Gráfico 1 não será exibido.")

# Procurar a primeira coluna numérica
num_col = None
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        num_col = col
        break

# Gráfico 2: Histograma
if num_col:
    st.write(f"### 📈 Gráfico 2: Histograma da coluna numérica '{num_col}'")
    fig2, ax2 = plt.subplots()
    ax2.hist(df[num_col].dropna(), bins=20, color='orange', edgecolor='black')
    ax2.set_xlabel(num_col)
    ax2.set_ylabel("Frequência")
    st.pyplot(fig2)
else:
    st.warning("⚠️ Nenhuma coluna numérica encontrada para o histograma.")

# Gráfico 3: Linha
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico de Pizza Simples")


data = {'Categoria': ['A', 'B', 'C', 'D'],
        'Valores': [25, 35, 20, 20]}
df = pd.DataFrame(data)

st.write("Dados:")
st.dataframe(df)


fig, ax = plt.subplots()
ax.pie(df['Valores'], labels=df['Categoria'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  

st.pyplot(fig)
