"""

### Parte 1 - Operações e Variáveis
Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 150<br>
Quantidade de Vendas de Pepsi = 130<br>
Preço Unitário da Coca = 1,50 <br>
Preço Unitário da Pepsi = 1,50<br>
Custo da Loja: 2.500,00

Use o bloco abaixo para criar todas as variáveis que precisar.
"""
qntd_coca = 150
qntd_pepsi = 130
precoUnitarioCoca = 1.50
precoUnitarioPepsi = 150
custodaloja = 2500

faturamentoPespi = 130 * 1.50
faturamentoCoca = 150 * 1.50

faturamento = faturamentoCoca + faturamentoPespi

lucro = faturamento - custodaloja

margem = lucro / faturamento


"""1. Qual foi o faturamento de Pepsi da Loja?"""

print(f"faturamento foi de {faturamentoPespi} ")


"""2. Qual foi o faturamento de Coca da Loja?"""

print(f"faturamento foi de {faturamentoCoca} ")


"""3. Qual foi o Lucro da loja?"""

print(f"lucro da loja foi de {lucro}")

"""4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual"""

print(f"a margem foi de {margem}")


"""### Parte 2 - Inputs e Strings

A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
Ex: 
Coca -> Código: BEB1300543<br>
Pepsi -> Código: BEB1300545<br>
Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
Vodka Smirnoff -> Código: BAC17675002<br>

Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
"""
cod = input("digite o codigo da bebida: ")

if "BEB" in cod:
    print("bebiba nao alcolica")
else:
    print("bebida alcolica")