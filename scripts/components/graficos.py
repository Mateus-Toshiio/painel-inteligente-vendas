import streamlit as st
import plotly.express as px

def criar_grafico_barras(df, x, y, titulo):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=titulo
    )

    fig.update_traces(
        texttemplate="R$ %{x:,.2f}",
        textposition="outside"
    )

    fig.update_layout(margin=dict(r=80),
                      yaxis_title="",
                      xaxis_title="",
                      xaxis_range=[x, df[x].max() * 1.2]
    )

    fig.update_yaxes(autorange="max reversed")

    return fig

def mostrar_graficos(faturamento_por_produto, faturamento_por_vendedor):
    col1, col2 = st.columns(2)

    with col1:
        fig = criar_grafico_barras(
            df=faturamento_por_produto,
            x="Valor",
            y="Produto",
            titulo="Faturamento por Produto"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = criar_grafico_barras(
            df=faturamento_por_vendedor,
            x="Valor",
            y="Vendedor",
            titulo="Faturamento por Vendedor"
        )

        st.plotly_chart(fig, use_container_width=True)