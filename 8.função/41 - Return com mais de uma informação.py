'''
# Como "retornar" mais de um objeto

- É possível retornar 2 "coisas"? 2 listas, 2 strings, 2 números...
    - Sim, basta retornar como uma tupla com 2 itens (vamos fazer um exemplo)
'''

def operacoesBasicas(num1, num2):
    soma = num1 + num2
    diferenca = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    return soma, diferenca, mult, div
#return fica como uma tupla

print(operacoesBasicas(10, 2))

#exercicio 5