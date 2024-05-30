'''
Escreva um programa em Python que recebe uma lista de números e encontra o maior número na lista.
O programa deve usar um laço for para iterar pelos elementos da lista e determinar o maior número.

'''

numeros = [
    12, 7, 45, 89, 32, 21, 34, 56, 78, 90,
    11, 23, 57, 43, 67, 88, 92, 31, 28, 73,
    19, 24, 46, 33, 54, 65, 87, 39, 40, 59,
    18, 20, 71, 83, 52, 29, 47, 62, 75, 93,
    15, 25, 36, 49, 60, 64, 77, 81, 22, 55
]
maiorNumero = 0
for numero in numeros:
    if numero > maiorNumero:
        maiorNumero = numero
print(maiorNumero)