def imprimirLinha():
    print("-" * 20)


produtos = ['apple tv', 'iphone X', 'mac', 'ipad', 'apple watch', 'airpods']

vendas = [1000, 150, 350, 270, 900, 750]

#metodos de print
#join imprime a lista só com os itens dessa lista, sem [] e '' e podendo acescentar o que quiser,
#como separando por virgulas ou pulando linha
print(', '.join(produtos))
print('\n'.join(produtos))

imprimirLinha()
#metodo split -> para pegar um banco de dados e transformar em uma lista

texto = 'airpods, apple watch, carregador, ipad, iphone 15, oculos'

lista = texto.split(', ')
print(lista)