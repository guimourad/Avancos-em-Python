'''
estrutura
Além de casos como o do enumerate, 
em que usamos uma função para transformar itens em tuplas porque isso ajuda o nosso código,
temos também listas de tuplas como algo comum dentro do Python.

lista = [
    tupla1,
    tupla2,
    tupla3,
    ]
    
ou seja

lista = [
    (valor1, valor2, valor3),
    (valor4, valor5, valor6),
    (valor7, valor8, valor9),
    ]

Exemplo:

Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.
Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:
'''
vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

#- Qual foi o faturamento de IPhone no dia 20/08/2020?
faturamento = 0

for item in vendas:
    #print(item)
    data, produto, cor, memoria, unidades, valorUnitario = item
    print(item)
#tambem posso colocar todas as variaveis direto no for
    
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valorUnitario
print(f'o valor vendido de iphone no dia 20 foi de R${faturamento}')

#data, produto, cor, memoria, unidades, valorUnitario = vendas[0]

#faturamento = unidades * valorUnitario
#print(faturamento)


#- Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?

produtoMaisVendido = ''
qtdeProdutoMaisVendido = 0

for item in vendas:
    data, produto, cor, memoria, unidades, valorUnitario = item
    if data == '21/08/2020':
        if unidades > qtdeProdutoMaisVendido:
            produtoMaisVendido = produto
            qtdeProdutoMaisVendido = unidades
print(f'meu produto mais vendido no dia 21 foi o {produtoMaisVendido} com {qtdeProdutoMaisVendido} unidades vendidas')
