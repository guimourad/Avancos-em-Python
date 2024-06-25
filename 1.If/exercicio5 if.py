
"""

## 1. Cálculo de Bônus

- Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas.<br> 
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.<br>
Caso contrário o valor de bônus do funcionário é 0.<br>
Print o bônus dos 3 funcionários
"""

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= 1000:
    bonus1 = 0.1 * vendas_funcionario1
    print(f"bonus do funcionario 1: {bonus1}")
else: 
    print("sem bonus")

if vendas_funcionario2 >= 1000:
    bonus2 = 0.1 * vendas_funcionario2
    print(f"bonus do funcionario 2: {bonus2}")
else: 
    print("sem bonus")

if vendas_funcionario3 >= 1000:
    bonus3 = 0.1 * vendas_funcionario3
    print(f"bonus do funcionario 3: {bonus3}")
else: 
    print("sem bonus")


"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 270 de bônus

## 2. Cálculo de bônus com uma nova regra

- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas<br>
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

Use as mesmas variáveis de vendas_funcionários
"""

if vendas_funcionario1 >=2000:
    bonus1 = 0.15 * vendas_funcionario1
    print(f"bonus de {bonus1} para o funcionario 1")
elif 1000<= vendas_funcionario1 <=2000:
    bonus2 = 0.1 * vendas_funcionario1
    print(f"bonus de {bonus2} para o funcionario 1")
else: 
    vendas_funcionario1 < 1000
    bonus3 = 0
    print(f"ganhou bonus de {bonus3}")


if vendas_funcionario2 >=2000:
    bonus1 = 0.15 * vendas_funcionario2
    print(f"bonus de {bonus1} para o funcionario 1")
elif 1000<= vendas_funcionario2 <=2000:
    bonus2 = 0.1 * vendas_funcionario2
    print(f"bonus de {bonus2} para o funcionario 1")
else: 
    vendas_funcionario2 < 1000
    bonus3 = 0
    print(f"ganhou bonus de {bonus3}")


if vendas_funcionario3 >=2000:
    bonus1 = 0.15 * vendas_funcionario3
    print(f"bonus de {bonus1} para o funcionario 1")
elif 1000<= vendas_funcionario3 <=2000:
    bonus2 = 0.1 * vendas_funcionario3
    print(f"bonus de {bonus2} para o funcionario 1")
else: 
    vendas_funcionario3 < 1000
    bonus3 = 0
    print(f"ganhou bonus de {bonus3}")

#crie seu código aqui
#obs: há 2 formas de fazer, com if dentro de if ou então com if e elif. Escolha a que você preferir

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 405 de bônus
"""