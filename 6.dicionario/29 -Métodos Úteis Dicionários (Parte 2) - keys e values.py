'''
# Listas importantes a partir do Dicionário

### Métodos importantes:

.keys() -> uma "lista" com todas as chaves do dicionario

.values() -> uma "lista" com todos os valores do dicionario

Obs: Se o dicionario for modificado, automaticamente essas variáveis são modificadas,
mesmo tendo sido criadas anteriormente
'''

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

chaves = vendas_tecnologia.keys() #-> lista com todas as chaves
print(chaves)

valores = vendas_tecnologia.values() #-> lista com todos os valores
print(valores)

vendas_tecnologia['copo stanley'] = 55
print(chaves)
print(valores)
print(list(chaves)) #-> transformando em uma lista
print(list(valores))


'''
### O for vai funcionar normal em dict_listas,
porque não deixa de ser uma lista de itens que pode ser percorrida (iterable),
mas o que aprendemos de lista não necessariamente se aplicam a essas dict_listas.

Para transformar as dict_listas em listas normais, usamos a função list:

- lista_chaves = list(dicionario.keys())


- Pode ser útil caso a gente queira fazer alguma organização das chaves.
Ex: Imprimir uma lista com os valores em ordem alfabética, de forma que todas as tvs fiquem juntas,
todos os iphone/ipad também e assim vai:
'''

for chave in vendas_tecnologia:
     print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))
print('-' * 40)

#agora se quisermos organizar isso, fazemos:
listaChaves = list(chaves)
print(listaChaves)
listaChaves.sort()
print(listaChaves)

for chave in listaChaves:
     print(f'{chave}: {vendas_tecnologia[chave]} unidades')
