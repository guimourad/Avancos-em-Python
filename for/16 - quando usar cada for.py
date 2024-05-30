produtos = ['iphone', 'ipad', 'airpods', 'macbook']
precos = [7000, 10000, 2000, 12000]

#preço do imposto
#quando for percorrer uma unica lista
for preco in precos:
    print(preco * 1.1)

#preco de cada produto
# percorrer duas listas, pegando os indices juntos de cada lista
for i in range (len(produtos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto, ':', preco)


#preco de cada produto com imposto
for i, preco in enumerate(precos):
    produto = produtos[i]
    print(f'preco de cada produto com imposto de 10%: {produto} : {preco * 1.1}')