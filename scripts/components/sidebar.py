import streamlit as st
import pandas as pd

def limpar_filtros():
    st.session_state["filtro_vendedor"] = "Todos"
    st.session_state["filtro_produto"] = "Todos"
    st.session_state["filtro_valor_min"] = 0.0
    st.session_state["filtro_valor_max"] = 0.0
    st.session_state["filtro_data_inicio"] = None
    st.session_state["filtro_data_fim"] = None

def mostrar_sidebar(df):
    with st.sidebar:
        st.header("Filtros")

        st.divider()
        st.subheader("Comercial")

        vendedores = ["Todos"] + sorted(df["Vendedor"].unique())

        vendedor = st.selectbox(
            "Vendedor",
            vendedores,
            key="filtro_vendedor"
        )

        produtos = ["Todos"] + sorted(df["Produto"].unique())

        produto = st.selectbox(
            "Produto",
            produtos,
            key="filtro_produto"
        )

        st.divider()
        st.subheader("Financeiro")

        col1, col2 = st.columns(2)

        with col1: valor_min = st.number_input("Mínimo", key="filtro_valor_min")

        with col2: valor_max = st.number_input("Máximo", key="filtro_valor_max")

        st.divider()
        st.subheader("Período")

        col1, col2 = st.columns(2)

        with col1: data_inicio = st.date_input("Início", value=None, format="DD/MM/YYYY", key="filtro_data_inicio")

        with col2: data_fim = st.date_input("Fim", value=None, format="DD/MM/YYYY", key="filtro_data_fim")

        st.button(
            "🧹 Limpar filtros",
            on_click=limpar_filtros,
            use_container_width=True
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