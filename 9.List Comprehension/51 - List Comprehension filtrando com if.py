'''
estrutura:
lista = [expressao for item in iterable if condicao]
'''

#digamos que eu queira criar uma lista de produtos que bateram a meta

meta =1000
vendasProdutos = [1500, 150, 2000, 1450]
produtos = ['vinho', 'cafe', 'vodka', 'suco']

#for tradicional
produtosBateuMeta = []
for venda, produto in enumerate(produtos):
    if vendasProdutos[venda] > meta:
        produtosBateuMeta.append(produto)

print(produtosBateuMeta)

#list comprehension

produtosBateuMeta2 = [produto for venda, produto in enumerate(produtos) if vendasProdutos[venda] > meta]
print(produtosBateuMeta2)