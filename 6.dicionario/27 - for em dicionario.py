'''
for chave in dicionario:
    faça alguma coisa
'''

vendasTecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#demonstrando o for
for chave in vendasTecnologia:
    print(f'{chave}: {vendasTecnologia[chave]} unidades')
#assim consigo usar a variavel chave para pegar a chave e o valor 

#- Qual o total de notebooks vendidos?
vendasNotebook = 0
for chave in vendasTecnologia:
    if 'notebook' in chave:
        vendasNotebook += vendasTecnologia[chave]
print(f'foram vendidas {vendasNotebook} unidades de notebook')