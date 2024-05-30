
def imprimirLinha():
    print("-" * 20)

produtos = ['apple tv', 'iphone X', 'mac', 'ipad', 'apple watch', 'airpods']

vendas = [1000, 150, 350, 270, 900, 750]

#trocar, adicionar e remover itens de uma lista

#trocar 
produtos[1] = "iphone 11"
print(f'novo produto: {produtos[1]}')

imprimirLinha()


#adicionar
produtos.append('iphone 15')
vendas.append(800)
print(f'produto adicionado: {produtos[6]}')

imprimirLinha()


#remover
#produtos.remove('iphone 11')
produtos.pop(1)
itemRemovido = produtos.pop(1)
print(f'produto removido: {itemRemovido}')
print(f'lista com a remoção: {produtos}')

imprimirLinha()

#tratar para ver se o item esta na lista
produtoRemover = "appleTv"
if produtoRemover in produtos:
    produtos.remove("appleTv")
else:
    print(f'{produtoRemover} nao esta na lista')

#ou

try:
    produtos.remove('apple tv')
    print(produtos)
except:
    print('appleTv nao esta na lista')

vendas.pop(0)
vendas.pop(1)
vendas.pop(4)