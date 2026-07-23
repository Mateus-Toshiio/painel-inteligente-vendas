import streamlit as st
import plotly.express as px

def mostrar_graficos(faturamento_por_produto, faturamento_por_vendedor):
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(faturamento_por_produto,
                     x="Valor",
                     y="Produto",
                     title="Faturamento por Produto")

        st.plotly_chart(fig,
                        use_container_width=True)

    with col2:
        ...