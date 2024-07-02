'''
# Um exemplo prático de List Comprehension

### O que faríamos se quisermos ordenar 2 listas "relacionadas"
'''
vendas_produtos = [1500, 150, 2100, 1950]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

listaAux = list(zip(vendas_produtos, produtos)) #-> zip junta as duas listas fazendo com que os elementos de cada lista
# vire uma lista de tuplas
listaAux.sort(reverse=True)
print(listaAux)

# for vendas, produtos in listaAux:
produtos = [produto for vendas, produto in listaAux]
print(produtos)

