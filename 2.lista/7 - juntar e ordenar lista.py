def imprimirLinha():
    print("-" * 20)


produtos = ['apple tv', 'iphone X', 'mac', 'ipad', 'apple watch', 'airpods']

vendas = [1000, 150, 350, 270, 900, 750]


#juntar listas e ordenar

novosProdutos = ['oculos', 'carregador']

produtos.extend(novosProdutos)
print(produtos)

vendaOculos = [150]
vendaCarregador = [450]

vendas.extend(vendaOculos)
vendas.extend(vendaCarregador)
print(vendas)
imprimirLinha()

#somar lista

somaVenda = vendaOculos[0] + vendaCarregador[0]

somaTodasVendas = 0
for venda in vendas:
    somaTodasVendas += venda

print(f'soma das vendas de oculos e carregador: {somaVenda}')
print(f'soma de todas as vendas: {somaTodasVendas}')

imprimirLinha()

#ordenar

produtos.sort()
print(produtos)

vendas.sort()
#vendas.sort(reverse=True) -> para imprimir em ordem decrescente
print(vendas)