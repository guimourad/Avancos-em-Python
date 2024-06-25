'''
as funcions são blocos de codigo que servem para um unico proposito, fazem uma ação especifica

def nome_funcao():
    faça alguma coisa
    faça outra coisa
    return valor_final
'''

#- Exemplo: vamos criar uma função de cadastro de um Produto.
# Essa função deve garantir que o produto cadastrado está em letra minúscula.

lista = []

def cadastrarProduto():

    produtos = input('digite o nome do produto: ')
    produtos = produtos.casefold()
    lista.append(produtos)
    print(f'produto {produtos} cadastrado com sucesso')

 


for i in range(3):
    cadastrarProduto()

print(f'produtos cadastrados: {lista}')
    


