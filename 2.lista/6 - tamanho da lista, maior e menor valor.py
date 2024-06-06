def imprimirLinha():
    print("-" * 20)


produtos = ['apple tv', 'iphone X', 'mac', 'ipad', 'apple watch', 'airpods']

vendas = [1000, 150, 350, 270, 900, 750]

#tamanho da lista, maior valor, menor valor
print(produtos)
print(vendas)
imprimirLinha()


totalItens = len(produtos)
print(f'temos {totalItens} itens')
imprimirLinha()

maiorVenda = max(vendas)
menorVenda = min(vendas)

print(f'o produto que mais vendeu teve {maiorVenda} vendas e o que menos vendeu teve {menorVenda} vendas')

i = vendas.index(maiorVenda)
i = vendas.index(menorVenda)
produtoMaisVendido = produtos[i]
produtoMenosVendido = produtos[i]


print(f'o produto mais vendido foi: {produtoMaisVendido} com {maiorVenda} vendas')
print(f'o produto menos vendido foi: {produtoMenosVendido} com {menorVenda} vendas')