def ranking_vendedores_por_faturamento(df):
    return df.groupby("Vendedor")["Valor"].sum().sort_values(ascending=False)

def ranking_produtos_mais_vendidos(df):
    return df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)
