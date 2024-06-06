vendas = ('mourad', '27/11/2004', '15/07/2024', 2000, 'estagiario')

nome = vendas[0]
dataNascimento = vendas[1] 
dataContracao = vendas[2]
salario = vendas[3]
cargo = vendas[4]

#isso é a mesma coisa do codigo de cima, que é chamado de unpacking
#em vez de pegar o indice de cada variavel, pode desmenbrar a tupla e usar dessa maneira
nome, dataNascimento, dataContracao, salario, cargo = vendas

print(nome)

#o enumerate que estava usando no for cria uma tupla

vendas = [1000, 2000, 3000, 4000, 5000]
funcionarios = ['mourad', 'guilherme', 'bia', 'rizatto', 'jade']
'''
for i, venda in enumerate(vendas):
    print(f'{funcionarios[i]} vendeu {venda} unidades'''

for item in enumerate(vendas):
    i, venda = item
    print(i)
    print(venda)
    print(item)
#nesse print, ele cria uma tupla com o indice e o valor desse indice, que é o mesma coisa que o unpacking faz
