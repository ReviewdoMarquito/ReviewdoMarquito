import streamlit as st
import pandas as pd
import plotly.express as px

sheet_name = 'Banco_de_Dados_Drive'
sheet_id = '1vQ4gIsfHwO4mUF9uSfLexQ-TXSRh4ZrpiBjj6KTWt6Y'

URL = url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

data1 = pd.read_csv(URL, skiprows=[1])

df1 = data1
df1.to_csv("novo dados.csv", encoding='utf-8', index=False)

data = pd.read_csv("novo dados.csv")

df = data

st.title("Review do Marquito - Avaliações")

restaurantes = df["Nome"].unique()
restaurante_selecionado = st.selectbox("Escolha um restaurante", restaurantes)

df_restaurante = df[df["Nome"] == restaurante_selecionado]

st.subheader("Detalhe da Avaliação")
st.dataframe(df_restaurante)

categorias = ["Simpatia", "Organização", "Preparo", "Apresentação", 
"Preço Justo?", "Destaque da Casa", "Clima (Música/Ruído)", 
"Limpeza", "Estacionamento/Acessibilidade", "Porções Justas?", "Vale a pena voltar?"]
medias = df_restaurante[categorias].mean()

fig = px.bar(
    x=categorias,
    y=medias,
    labels={'x': 'Categoria', 'y': 'Nota Média'},
    title="Média das Notas por Categoria"
)

st.plotly_chart(fig)


