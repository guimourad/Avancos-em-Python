


produtos = ['apple tv', 'iphone X', 'mac', 'ipad', 'apple watch', 'airpods']

vendas = [1000, 150, 350, 270, 900, 750]

#como descobrir o indice de uma lista

i = produtos.index('iphone X')
qtdeEstoque = vendas[i]

print(i)
print(produtos[i])
print(f'quantidade de vendas do mouse é de {qtdeEstoque}')