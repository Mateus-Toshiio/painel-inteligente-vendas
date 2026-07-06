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
for produto, quantidade in resumo['ranking_produtos_mais_vendidos'].items():
    print(f"{posicao}° {produto} - {quantidade}")
    posicao += 1

print("\nRanking de Vendedores\n")
posicao = 1
for vendedor, valor in resumo["ranking_vendedores_por_faturamento"].items():
    print(f"{posicao}° {vendedor} - R$ {valor:,.2f}")
    posicao += 1