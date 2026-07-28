import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():
    try:
        df = pd.read_csv("dados/vendas.csv")
    except FileNotFoundError:
        st.error("Arquivo não encontrado.")
        st.stop()

    df['Data'] = pd.to_datetime(df['Data'])
    return df