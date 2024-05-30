"""
1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]


vendas_1sem.extend(vendas_2sem)

print(vendas_1sem)
maiorValor = max(vendas_1sem)
menorValor = min(vendas_1sem)

print(f"o valor de vendas do melhor mes foi de {maiorValor} e o do pior mes foi de {menorValor}")

"""
2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""

iMaior = vendas_1sem.index(maiorValor)
iMenor = vendas_1sem.index(menorValor)

melhorMes = meses[iMaior]
piorMes = meses[iMenor]

print(f'O melhor mês do ano foi {melhorMes} com {maiorValor} vendas ')
print(f'O pior mês do ano foi {piorMes} com {menorValor} vendas ')

faturamento = sum(vendas_1sem)

print(f'o faturamento foi de {faturamento}')

percentual = (maiorValor / faturamento)
print(f'o melhor mes representou {percentual:.2%} das vendas totais')

"""
 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""

top3 = []

top3.append(maiorValor)

print(top3)

vendas_1sem.remove(maiorValor)
segundoValor = max(vendas_1sem)
top3.append(segundoValor)
print(top3)

vendas_1sem.remove(segundoValor)
terceiroValor = max(vendas_1sem)
top3.append(terceiroValor)
print(f'os 3 maiores valores sao: {top3}')

