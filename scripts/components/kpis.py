import streamlit as st

def mostrar_kpis(
        faturamento_total,
        quantidade_vendas,
        maior_valor_venda,
        menor_valor_venda,
        valor_medio_venda
):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(label="Faturamento", value=f"R$ {faturamento_total:,.2f}")
    
    with col2:
        st.metric(label="Vendas", value=quantidade_vendas)

    with col3:
        st.metric(label="Maior Venda", value=f"R$ {maior_valor_venda:,.2f}")

    with col4:
        st.metric(label="Menor Venda", value=f"R$ {menor_valor_venda:,.2f}")

    with col5:
        st.metric(label="Ticket Médio", value=f"R$ {valor_medio_venda:,.2f}")