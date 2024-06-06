#break -> interrompe e fnaliza o for
#continue -> interrompe e vai para o proximo item do for

vendas = [10, 20, 30, 40, 50]

#caso 1 -> se todas as vendas forem a cima da media, a loja ganha bonus
meta = 15

for venda in vendas:
    if venda < meta:
        print('a loja nao ganha bonus')
        break
    print(venda)



#caso 2 -> exiba quem bateu a meta
vendedores = ['gui', 'bia', 'thi', 'joao', 'jade']
meta = 28

for venda in vendas:
    if venda < meta:
        continue
    print(venda)

