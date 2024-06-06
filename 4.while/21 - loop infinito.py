#sempre que for usar o comando while, tenha certeza que o programa vai terminar em algum momento

#Digamos que temos uma lista de vendedores e as quantidades vendidas
#e queremos identificar todos os vendedores que bateram a meta de 50 vendas.

vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]
vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50
i = 0
while vendas[i] > meta:
    print(f'{vendedores[i]} bateram a meta')
    i += 1

#for i, venda in enumerate(vendas):
#    if venda > meta:
#        print(f'{vendedores[i]} bateram a meta')