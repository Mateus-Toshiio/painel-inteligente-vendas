def aplicar_filtros(
        df,
        vendedor=None,
        produto=None,
        data_inicio=None,
        data_fim=None,
        valor_min=None,
        valor_max=None
):
    
    if vendedor is not None:
        df = df[df['Vendedor'] == vendedor]

    if produto is not None:
        df = df[df['Produto'] == produto]

    if data_inicio is not None:
        df = df[df['Data'] >= data_inicio]

    if data_fim is not None:
        df = df[df['Data'] <= data_fim]

    if valor_min is not None:
        df = df[df['Valor'] >= valor_min]

    if valor_max is not None:
        df = df[df['Valor'] <= valor_max]

    return df