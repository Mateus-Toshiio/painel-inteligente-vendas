import pandas as pd

def carregar_dados():
    df = pd.read_csv("dados/vendas.csv")

    df['Data'] = pd.to_datetime(df['Data'])
    return df