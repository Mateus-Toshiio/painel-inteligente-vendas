import streamlit as st
import pandas as pd

def mostrar_sidebar(df):

    st.sidebar.header("Filtros TESTE")

    vendedores = ["Todos"] + sorted(df["Vendedor"].unique())

    vendedor = st.sidebar.selectbox(
        "Vendedor",
        vendedores
    )

    produtos = ["Todos"] + sorted(df["Produto"].unique())

    produto = st.sidebar.selectbox(
        "Produto",
        produtos
    )

    valor_min = st.sidebar.number_input(
        "Valor Mínimo"
    )

    valor_max = st.sidebar.number_input(
        "Valor Máximo"
    )

    data_inicio = st.sidebar.date_input(
        "Data Início",
        value=None,
        format="DD/MM/YYYY"
    )

    data_fim = st.sidebar.date_input(
        "Data Fim",
        value=None,
        format="DD/MM/YYYY"
    )

    if data_inicio is not None:
        data_inicio = pd.to_datetime(data_inicio)

    if data_fim is not None:
        data_fim = pd.to_datetime(data_fim)

    if valor_min == 0:
        valor_min = None

    if valor_max == 0:
        valor_max = None

    if vendedor == "Todos":
        vendedor = None

    if produto == "Todos":
        produto = None

    return {
        "vendedor": vendedor,
        "produto": produto,
        "valor_min": valor_min,
        "valor_max": valor_max,
        "data_inicio": data_inicio,
        "data_fim": data_fim
    }