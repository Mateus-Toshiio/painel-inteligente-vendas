from analise import carregar_dados, resumo_geral

print("=" * 50)
print("PAINEL INTELIGENTE DE VENDAS")
print("=" * 50)

df = carregar_dados()

resumo = resumo_geral(df)

posicao = 1


print(f"\nQuantidade de vendas: {resumo['quantidade_vendas']}")
print(f"Faturamento total: R$ {resumo['faturamento_total']:,.2f}")
print(f"Maior venda: R$ {resumo['maior_valor_venda']:,.2f}")
print(f"Menor venda: R$ {resumo['menor_valor_venda']:,.2f}")
print(f"Média das vendas: R$ {resumo['valor_medio_venda']:,.2f}")

print("\nProdutos mais vendidos:\n")

for posicao, (produto, quantidade) in enumerate(resumo['ranking_produtos_mais_vendidos'].items(), start=1):
    print(f"{posicao}° {produto} - {quantidade}")

print("\nRanking de Vendedores\n")
for posicao, (vendedor, valor) in enumerate(resumo['ranking_vendedores_por_faturamento'].items(), start=1):
    print(f"{posicao}° {vendedor} - R$: {valor:,.2f}")