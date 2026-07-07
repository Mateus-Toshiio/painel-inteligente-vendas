import pandas as pd

def carregar_dados():
    df = pd.read_csv("dados/vendas.csv")
    return df