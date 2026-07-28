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

    return df_exibicao

def mostrar_tabela_vendas(df):
    st.subheader("Vendas")

    df_exibicao = formatar_tabelas(df)

    st.dataframe(
        df_exibicao,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Data": st.column_config.DateColumn(
                "Data",
                width=110
            ),
            "Vendedor": st.column_config.TextColumn(
                "Vendedor",
                width="medium"
            ),
            "Produto": st.column_config.TextColumn(
                "Produto",
                width="medium"
            ),
            "Quantidade": st.column_config.NumberColumn(
                "Quantidade",
                width=30
            ),
            "Valor": st.column_config.NumberColumn(
                "Valor",
                width=130,
                format="R$ %.2f"
            )
        }
    )