from indicadores import (faturamento_total, quantidade_vendas, maior_valor_venda, menor_valor_venda, valor_medio_venda)
from rankings import (ranking_produtos_mais_vendidos, ranking_vendedores_por_faturamento)

def resumo_geral(df):
    """Calcula as principais métricas."""

    resumo = {
        "quantidade_vendas": quantidade_vendas(df),
        "faturamento_total": faturamento_total(df),
        "maior_valor_venda": maior_valor_venda(df),
        "menor_valor_venda": menor_valor_venda(df),
        "valor_medio_venda": valor_medio_venda(df),
        "ranking_vendedores_por_faturamento": ranking_vendedores_por_faturamento(df).head(3),
        "ranking_produtos_mais_vendidos": ranking_produtos_mais_vendidos(df).head(3)
    }

    return resumo