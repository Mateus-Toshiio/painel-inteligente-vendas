import streamlit as st
from scripts.components.kpis import mostrar_kpis


from scripts.carregamento import carregar_dados
from scripts.analise import resumo_geral

st.set_page_config(
    page_title="Painel Inteligente de Vendas",
    layout="wide"
)

st.title("Painel Inteligente de Vendas")

df = carregar_dados()
resumo = resumo_geral(df)

mostrar_kpis(
    faturamento_total=resumo["faturamento_total"],
    quantidade_vendas=resumo["quantidade_vendas"],
    maior_valor_venda=resumo["maior_valor_venda"],
    menor_valor_venda=resumo["menor_valor_venda"],
    valor_medio_venda=resumo["valor_medio_venda"]
)

