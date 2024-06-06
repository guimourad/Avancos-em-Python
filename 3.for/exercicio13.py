'''
# Exercícios

## 1. Calculando % de uma lista

Faremos algo parecido com "filtrar" uma lista.
Mais pra frente no curso aprenderemos outras formas de fazer isso,
mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores
e ao invés de saber todos os vendedores que bateram a meta,
eu quero conseguir calcular o % de vendedores que bateram a meta.
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.
'''

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

#com lista auxiliar
vendedorBateuMeta = []

for venda in vendas:
    if venda[1] > meta:
        vendedorBateuMeta.append(venda[0])
print(vendedorBateuMeta)
porcentagem = len(vendedorBateuMeta) / len(vendas)
print(f'{porcentagem:.2%} dos vendedores bateram a meta')

print('¨\n¨')
#calcular direto na lista
vendedorAcimaMeta = 0

for venda in vendas:
    if venda[1] > meta:
        vendedorAcimaMeta += 1
print(f'{vendedorAcimaMeta / len(vendas):.2%} dos vendedores bateram a meta')

print('¨\n¨')


### Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?

melhorVendedor = ''
maiorVenda = 0
for venda in vendas:
    #percorre cada item da lista, se for maior que o anterior, passa a ser o maior, e isso ate percorrer toda a lista
    if venda[1] > maiorVenda:
        maiorVenda = venda[1]
        melhorVendedor = venda[0]
print(f'o melhor vendedor foi {melhorVendedor} com {maiorVenda} vendas')
