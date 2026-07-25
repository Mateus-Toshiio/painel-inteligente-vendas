import streamlit as st

def formatar_tabelas(df):
    df_exibicao = df[
        [
            "Data",
            "Vendedor",
            "Produto",
            "Quantidade",
            "Valor"
        ]
    ].copy()

    df_exibicao["Data"] = df_exibicao["Data"].dt.strftime("%d/%m/%Y")

    df_exibicao["Valor"] = (
        "R$ "
        + df_exibicao["Valor"]
            .map(lambda x: f"{x:,.2f}")
            .str.replace(",", "X")
            .str.replace(".", ",")
            .str.replace("X", ".")
    )

    return df_exibicao

def mostrar_tabela_vendas(df):
    st.subheader("Vendas")

    df_exibicao = formatar_tabelas(df)

    st.dataframe(
        df_exibicao,
        use_container_width=True
    )