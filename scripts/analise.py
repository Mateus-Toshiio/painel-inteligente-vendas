import pandas as pd


def carregar_dados():
    """Lê o arquivo CSV e devolve um DataFrame."""

    df = pd.read_csv("dados/vendas.csv")
    return df


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

def ranking_vendedores_por_faturamento(df):
    return df.groupby("Vendedor")["Valor"].sum().sort_values(ascending=False)

def ranking_produtos_mais_vendidos(df):
    return df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

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