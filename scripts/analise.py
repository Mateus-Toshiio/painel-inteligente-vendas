from indicadores import (faturamento_total, quantidade_vendas, maior_valor_venda, menor_valor_venda, valor_medio_venda)
from rankings import (ranking_produtos_mais_vendidos, ranking_vendedores_por_faturamento)
from filtros import (aplicar_filtros)

def resumo_geral(df,
        vendedor=None,
        produto=None,
        data_inicio=None,
        data_fim=None,
        valor_min=None,
        valor_max=None):

    df = aplicar_filtros(df,
        vendedor=vendedor,
        produto=produto,
        data_inicio=data_inicio,
        data_fim=data_fim,
        valor_min=valor_min,
        valor_max=valor_max)

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