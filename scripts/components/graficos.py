import streamlit as st
import plotly.express as px

def mostrar_graficos(faturamento_por_produto, faturamento_por_vendedor):
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(faturamento_por_produto,
                     x="Valor",
                     y="Produto",
                     title="Faturamento por Produto")
        
        fig.update_traces(texttemplate="R$ %{x:,.2f}",
                          textposition="outside")
        
        fig.update_layout(margin=dict(r=80),
                          xaxis_title="",
                          yaxis_title="",
                          xaxis_range=[0, faturamento_por_produto["Valor"].max() * 1.2,],
                          )
        
        fig.update_yaxes(autorange="max reversed")

        st.plotly_chart(fig,
                        use_container_width=True)

    with col2:
        ...