#estrutura -> tupla = (valor, valor, valor)
#tupla é uma lista imutavel, ou seja, nao pode modificar

#é mais eficiente
#protege a base de dados por ser imutavek
#muito usado para dados heterogeneos

vendas = ('mourad', '27/11/2004', '15/07/2024', 2000, 'estagiario')

nome = vendas[0]
dataNascimento = vendas[1] 
dataContracao = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print(nome)

