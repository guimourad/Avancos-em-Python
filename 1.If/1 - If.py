"""


meta = 50000
qtdeVendida = 3000

if qtdeVendida > meta:
    print("meta batida")
else:
    print("meta nao batida")

"""

metaFuncionario = 10000
metaLoja = 25000
vendaFuncionario = 5000
vendaLoja = 20000

"""
if vendaFuncionario > metaFuncionario and vendaLoja > metaLoja:
    bonus = 0.03 * vendaFuncionario
    print(f"o bonus do funicionario foi de {bonus}")
else:
    print("nao ganhou bonus")

"""

metaNota = 9
notaFuncionario = 5

if notaFuncionario > metaNota or (vendaFuncionario > metaFuncionario and vendaLoja > metaLoja):
    bonus = 0.03 * vendaFuncionario
    print(f'Bonus do funcionario foi de {bonus}')
else:
    print('Funcionário não ganhou bônus')





