'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, 
que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.
'''

'''
##### Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.

Dica: lembre dos operadores // e % mostrados em exercícios anteriores
Dica: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10. Ex: 7 // 3 = 2; 10 // 3 = 3
Dica: numero % 10 vai te dar o resto da divisão do número por 10. Ex: 7 % 3 = 1; 10 % 3 = 1; 15 % 3 = 0
'''

#### 1. comprar latas de apenas 18 litros: (apenas latas inteiras)
def areaPintada():
    area = int(input('qual a area que vai ser pintada (m²): '))
    return area

def calcularLitrosTinta(area):
    litros = area / 6
    return litros

def calcularLatas(litros):
    latas = litros / 18
    if latas > int(latas):
        latas =  int(latas) + 1 
    return latas

def calcularCusto(latas):
    preco = latas * 80
    return preco


area = areaPintada()
litros = calcularLitrosTinta(area)
latas = calcularLatas(litros)
preco = calcularCusto(latas)
print(f'latas: {latas}')
print(f'preco {preco}')


##### 2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)
def areaPintada():
    area = int(input('qual a area que vai ser pintada (m²): '))
    return area

def calcularLitrosTinta(area):
    litros = area / 6
    return litros

def calcularLatas(litros):
    galao = litros / 3.6
    if galao > int(galao):
        galao =  int(galao) + 1 
    return galao

def calcularCusto(galao):
    preco = galao * 25
    return preco


area = areaPintada()
litros = calcularLitrosTinta(area)
galao = calcularLatas(litros)
preco = calcularCusto(galao)
print(f'galao: {galao}')
print(f'preco {preco}')


