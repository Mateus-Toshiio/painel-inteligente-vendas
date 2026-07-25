import streamlit as st

from scripts.components.graficos import mostrar_graficos
from scripts.components.kpis import mostrar_kpis
from scripts.carregamento import carregar_dados
from scripts.analise import resumo_geral
from scripts.components.sidebar import mostrar_sidebar
from scripts.filtros import aplicar_filtros
from scripts.components.tabela import mostrar_tabela_vendas

st.set_page_config(
    page_title="Painel Inteligente de Vendas",
    layout="wide"
)

st.title("Painel Inteligente de Vendas")

df = carregar_dados()

filtros = mostrar_sidebar(df)

df_filtrado = aplicar_filtros(df, **filtros)

resumo = resumo_geral(df_filtrado)

mostrar_kpis(
    faturamento_total=resumo["faturamento_total"],
    quantidade_vendas=resumo["quantidade_vendas"],
    maior_valor_venda=resumo["maior_valor_venda"],
    menor_valor_venda=resumo["menor_valor_venda"],
    valor_medio_venda=resumo["valor_medio_venda"]
)

st.divider()

mostrar_graficos(
    faturamento_por_produto=resumo["faturamento_por_produto"],
    faturamento_por_vendedor=resumo["faturamento_por_vendedor"]
)

st.divider()

mostrar_tabela_vendas(df_filtrado)