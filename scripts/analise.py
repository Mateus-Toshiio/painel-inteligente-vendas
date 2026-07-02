import pandas as pd


def carregar_dados():
    """Lê o arquivo CSV e devolve um DataFrame."""

    df = pd.read_csv("dados/vendas.csv")
    return df


def resumo_geral(df):
    """Calcula as principais métricas."""

    resumo = {
        "quantidade_vendas": len(df),
        "faturamento_total": df["Valor"].sum(),
        "maior_venda": df["Valor"].max(),
        "menor_venda": df["Valor"].min(),
        "media_vendas": df["Valor"].mean(),
    }

    return resumo