'''
estrutura:
itens_dicionario = dicionario.items()

ou então:

for item in dicionario.items()
    cada item do dicionario em formato de tupla
'''

vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

itensDicionario = vendas_tecnologia.items() # -> transforma um dicionario em uma lista de tuplas, tendo uma melhor vizualizaçãao
print(itensDicionario)

for produto, qtde in vendas_tecnologia.items():
    print(f'{produto} : {qtde}')


print('*' * 20)
#quais produtos venderam mais que 500 unidades?
#forma 1: usando apenas o dicionario e as chaves

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print(f'{chave} : {vendas_tecnologia[chave]}')
print('*' *20)
#forma 2: usando o comando .items()

for produto, qtde in vendas_tecnologia.items():
    if  qtde > 5000:
        print(f'{produto} : {qtde}')



