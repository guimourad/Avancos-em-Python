#adicionar itens
'''
dicionario = {}

dicionario[chave] = valor

outra opção:

dicionario.update({chave: valor, chave: valor})
'''

lucro1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}

#adicionando 1 item
print(lucro1tri)
lucro1tri['abril'] = 88000
print(lucro1tri)


#adicionando vários itens ou um dicionário a outro
lucro1tri.update({'abril': 88000, 'maio': 89000, 'junho': 120000})
#lucro_1tri.update(lucro_2tri)
print(lucro1tri)


#adicionando um item já existente (manualmente ou pelo update)
lucro1tri['janeiro'] = 88000
print(lucro1tri)


'''
- Modificar itens:
#é a mesma forma que usamos para adicionar um item
Da mesma forma que adicionamos 1 valor, caso essa chave já exista o item é apenas modificado.

dicionario[chave] = valor

Vamos modificar o lucro de fevereiro:
(Lembrando: caso o item não exista, ele vai criar o item no dicionário)
'''

lucroFev = 85000
lucro1tri['fevereiro'] = lucroFev
print(lucro1tri)


'''
- Remover itens:

del dicionario[chave]

ou então

valor = dicionario.pop(chave)

mas cuidado com:

del dicionario    ->    que é diferente de dicionario.clear()
'''

#removendo o mês de junho
del lucro1tri['junho'] # -> remove do dicionario
lucroMaio = lucro1tri.pop('maio') # -> remove do dicionario e adiciona em uma variavel
print(lucro1tri)
print(lucroMaio)

del lucro1tri # -> deleta todo o dicionario
lucro1tri.clear() # -> limpa o dicionario mas continua existindo

#obs: o del também funciona para listas, caso queira usar
#del lista[i]
funcionarios = ['João', 'Lira', 'Maria', 'Ana', 'Paula']
del funcionarios[0]
print(funcionarios)

