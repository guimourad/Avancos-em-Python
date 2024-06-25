'''
# Quantidade Indefinidas de Argumentos

Utilidade:

Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

Estrutura:

*args para positional arguments -> argumentos vêm em formato de tupla

def minha_funcao(*args):
    ...


**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):
    ...
'''

def minhaSoma(*numeros): #_> passo quantos parametros eu quiser
    print(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(minhaSoma(1, 2, 3, 5, 7, 9, 13, 18))

def precoFinal(preco, **adicionais): #_> argumento que pode receber varias informacoes ao mesmo tempo, sendo uma chave e um valor
    print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantiaExtra' in adicionais:
        preco += adicionais['garantiaExtra'] 
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print(precoFinal(1000, desconto = 0.1, garantiaExtra = 100, imposto = 0.3))

