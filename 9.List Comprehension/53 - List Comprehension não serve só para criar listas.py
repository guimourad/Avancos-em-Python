'''
# List Comprehension não serve só para criar uma lista, serve para qualquer ação em iterable

### Exemplo:
- Vamos calcular quantos % das vendas o meu top 5 produtos representa das vendas totais
'''
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

#for
totalTop5 = 0
for i, produto in enumerate(produtos):
    if produto in top5:
        totalTop5 += vendas[i]
print(totalTop5)
print(f'top5 representou {totalTop5/sum(vendas):0.1%} das vendas')



#list comprehension
totalTop5 = sum(vendas[i] for i, produto in enumerate(produtos) if produto in top5)


print(totalTop5)
print(f'top5 representou {totalTop5/sum(vendas):0.1%} das vendas')