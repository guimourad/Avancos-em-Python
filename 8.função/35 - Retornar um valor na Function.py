'''
estrutura:
def nome_funcao():
    return valor_final

. as variaveis de uma funcion só existem nela mesma

'''

#- Exemplo: vamos criar uma função de cadastro de um Produto.
# Essa função deve garantir que o produto cadastrado está em letra minúscula.

def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar')
    produto = produto.casefold()
    produto = produto.strip() #-> remover espaços no inicio e final
    return produto

#print(cadastrar_produto())
produtoCadastrado = cadastrar_produto()
print(produtoCadastrado)