'''
O custo da lata é 80/18 = 4,44 R$/L

O custo do galão é 25/3,6 = 6,94 R$/L

A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas.
Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:

Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.

Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros.
Então devemos comprar pelo menos 5 latas e avaliar o que falta,
se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total.
Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar 2 galões.

Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros.
Então devemos comprar pelo menos 5 latas e avaliar o que falta,
se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total.
Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar uma lata.

3 galões custam 75 reais, 4 galões custam 100 reais.
Então, se for possível completar com até 3 galões escolhe-se galões.
Qualquer quantidade maior que 3 galões, usa-se latas.

Podemos ir ao exercício:
'''

#pegar a area a ser pintada
def areaPintada():
    area = int(input('qual a area que vai ser pintada (m²): '))
    return area


#pegar quantos litros de tinta eu vou precisar
def calcularLitrosTinta(area):
    litros = area / 6
    return litros


#calcular quantas latas e quantos galoes vou precisar
    #calcular quantas latas inteiras eu vou precisar
    #calcular quantos litros faltam comprar
    #calcular quanto custa preencher esses litros que faltam com galoes
    #calcular quanto custa preencher esses litros que faltam com latas
    #escolher a opçao mais barata
def calcularQtdeLatasGalao(litros):
    latas = 0
    galao = 0

    latasInteiras = int(litros / 18) #-> descobrir quantas latas de tinta vou precisar

    litrosFaltam = litros % 18 #-> me da o resto da divisao, que seria quantos litros faltam comprar

    #se for preencher com latas
    custoExtrasLatas = 1 * 80

    #se for preencher com galao
    galao =  litrosFaltam / 3.6 #descobrir quantos galoes vou precisar comprar para x litros que estao faltando
    if galao > int(galao):
        galao = int(galao) + 1

    custoExtraGalao = galao * 25

    if custoExtrasLatas < custoExtraGalao:
        latas = latasInteiras + 1
        galao = 0
    else:
        latas = latasInteiras

    return latas, galao


#calcular o total
def calcularCusto(latas, galao):
    custoLata = latas * 80
    custoGalao = galao* 25
    custoTotal = custoLata + custoGalao
    return custoTotal



area = areaPintada()
litros = calcularLitrosTinta(area)
latas, galao = calcularQtdeLatasGalao(litros)


custo = calcularCusto(latas, galao)

print(f'litros: {litros}')
print(f'latas: {latas}')
print(f'galao: {galao}')
print(f'custo: {custo}')
