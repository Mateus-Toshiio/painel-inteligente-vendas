import streamlit as st

from scripts.utils.formatacao import formatar_moeda

def mostrar_kpis(
        faturamento_total,
        quantidade_vendas,
        maior_valor_venda,
        menor_valor_venda,
        valor_medio_venda
):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(label="💰 Faturamento Total", value=formatar_moeda(faturamento_total), border=True)
    
    with col2:
        st.metric(label="🛒 Quantidade de Vendas", value=quantidade_vendas, border=True)

    with col3:
        st.metric(label="📈 Maior Venda", value=formatar_moeda(maior_valor_venda), border=True)

    with col4:
        st.metric(label="📉 Menor Venda", value=formatar_moeda(menor_valor_venda), border=True)

    with col5:
        st.metric(label="📊 Valor Médio", value=formatar_moeda(valor_medio_venda), border=True)