from scripts.indicadores import (faturamento_total, quantidade_vendas, maior_valor_venda, menor_valor_venda, valor_medio_venda, faturamento_por_produto, faturamento_por_vendedor, faturamento_por_mes)

def resumo_geral(df):

    resumo = {
        "quantidade_vendas": quantidade_vendas(df),
        "faturamento_total": faturamento_total(df),
        "maior_valor_venda": maior_valor_venda(df),
        "menor_valor_venda": menor_valor_venda(df),
        "valor_medio_venda": valor_medio_venda(df),
        "faturamento_por_produto": faturamento_por_produto(df),
        "faturamento_por_vendedor": faturamento_por_vendedor(df),
        "faturamento_por_mes": faturamento_por_mes(df),
    }

    return resumo