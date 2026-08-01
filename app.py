import streamlit as st

from scripts.components.graficos import mostrar_graficos, criar_grafico_evolucao
from scripts.components.kpis import mostrar_kpis
from scripts.carregamento import carregar_dados
from scripts.analise import resumo_geral
from scripts.components.sidebar import mostrar_sidebar
from scripts.filtros import aplicar_filtros
from scripts.components.tabela import mostrar_tabela_vendas
from scripts.utils.estilos import carregar_css

st.set_page_config(
    page_title="Painel de Vendas",
    layout="wide"
)

carregar_css()

st.title("📊 Painel de Vendas")

st.caption("Acompanhe indicadores, gráficos e vendas utilizando os filtros disponíveis na barra lateral.")

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

fig_evolucao = criar_grafico_evolucao(
    resumo["faturamento_por_mes"]
)

st.plotly_chart(
    fig_evolucao,
    use_container_width=True,
    config={"displayModeBar": False}
)

st.divider()

mostrar_tabela_vendas(df_filtrado)