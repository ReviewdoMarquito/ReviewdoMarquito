import streamlit as st
import pandas as pd
import plotly.express as px

sheet_name = 'Banco_de_Dados_Drive'
sheet_id = '1vQ4gIsfHwO4mUF9uSfLexQ-TXSRh4ZrpiBjj6KTWt6Y'

URL = url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

data = pd.read_csv(URL)

df = data

st.logo("logo.jpg", *, size="medium", link="https://www.instagram.com/reviewdomarquito/", icon_image=None)
st.image("faces.png")
st.title("Review do Marquito - Avaliações")

restaurantes = df["Nome"].unique()
restaurante_selecionado = st.selectbox("Escolha um restaurante", restaurantes)

df_restaurante = df[df["Nome"] == restaurante_selecionado]

st.subheader("Detalhe da Avaliação")
st.dataframe(df_restaurante)

categorias = ["Agilidade", "Simpatia", "Organização", "Sabor", "Preparo", "Apresentação", 
"Cartela de Bebidas", "Preço Justo?", "Destaque da Casa", "Conforto", "Clima (Música/Ruído)", 
"Limpeza", "Estacionamento/Acessibilidade", "Preço vs Qualidade", "Porções Justas?", "Vale a pena voltar?"]
medias = df_restaurante[categorias].mean()

fig = px.bar(
    x=categorias,
    y=medias,
    labels={'x': 'Categoria', 'y': 'Nota Média'},
    title="Média das Notas por Categoria"
)

st.plotly_chart(fig)


