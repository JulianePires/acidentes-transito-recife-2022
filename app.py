import streamlit as st

DADOS_URL = "./acidentes2022.csv"

st.title("Acidentes de trânsito com e sem vitimas na cidade de Recife - 2022")
st.markdown(
    "Esta aplicação é um dashboard Streamlit que pode ser utilizado "
    "para analise das estatísticas dos acidentes de trânsito na cidade de Recife 🏙💥🚗"
)

## Indices de vítimas por bairro
