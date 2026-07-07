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