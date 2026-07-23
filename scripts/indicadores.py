def faturamento_total(df):
    return df["Valor"].sum()

def quantidade_vendas(df):
    return len(df)

def maior_valor_venda(df):
    return df["Valor"].max()

def menor_valor_venda(df):
    return df["Valor"].min()

def valor_medio_venda(df):
    return df["Valor"].mean()

def faturamento_por_produto(df):
    return df.groupby("Produto")["Valor"].sum().sort_values(ascending=False).reset_index()

def faturamento_por_vendedor(df):
    return df.groupby("Vendedor")["Valor"].sum().sort_values(ascending=False).reset_index()