from analise import carregar_dados, resumo_geral

print("=" * 50)
print("PAINEL INTELIGENTE DE VENDAS")
print("=" * 50)

df = carregar_dados()

resumo = resumo_geral(df)

print(f"\nQuantidade de vendas: {resumo['quantidade_vendas']}")
print(f"Faturamento total: R$ {resumo['faturamento_total']:,.2f}")
print(f"Maior venda: R$ {resumo['maior_venda']:,.2f}")
print(f"Menor venda: R$ {resumo['menor_venda']:,.2f}")
print(f"Média das vendas: R$ {resumo['media_vendas']:,.2f}")