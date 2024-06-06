#crie um programa para fazer uma consulta de estoque. O usuario do programa deve inserir o nome do produto e, caso ele nao exista na lista, ele é avisado.
#Caso exista, o programa deve dizer a quantidade de unidades do produto


produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
estoque = [1000, 150, 350, 270, 900]

produto = input('insira o nome do produto que deseja consultar: ')
if produto in produtos:

    i = produtos.index(produto)

    qtdeEstoque = estoque[i]

    print(f'a quantidade de {produto} em estoque é de {qtdeEstoque}')
else:
    print("nao existe em estoque")
