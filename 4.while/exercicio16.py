'''
Exercícios

 1. Input até o usuário parar

Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs)
e adicionar em uma lista.

O programa deve continuar rodando até o input ser vazio, ou seja,
o usuário apertar enter sem digitar nenhum produto ou quantidade.

Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha.
Sugestão para sua lista de produtos vendidos:
'''

'''
vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]
'''

vendas = []

while True:
    produtos = input('nome do produto <enter para encerrar>: ')
    if produtos == '':
        break
    else:
        
        quantidade = int(input('quantidade <enter para encerrar>: '))
        vendas.append([produtos, quantidade])

print(vendas)

'''
produtos = input('nome do produto <enter para encerrar>: ')
quantidade = int(input('quantidade <enter para encerrar>: '))

while produtos:
    vendas.append([produtos, quantidade])
    produtos = input('nome do produto <enter para encerrar>: ')
    quantidade = int(input('quantidade <enter para encerrar>: '))
print(vendas)

'''


