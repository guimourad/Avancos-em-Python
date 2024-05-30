#usamos o while quando queremos repetir um codigo de forma indeterminada até uma condição se tornar verdadeira/falsa
#a logica é: enquanto uma condição for verdadeira, o while executa o codigo. Assim que ela terminar de ser verdadeira, o codigo sai do while

#- Exemplo: Quando criamos automações na internet
#- Exemplo2: Crie um programa que funcione como o registro de vendas de uma empresa.

#Nele, a pessoa deve inserir o nome do produto e o produto deve ser adicionado na lista de venda.
#Enquanto o usuário não encerrar o programa, significa que ele está registrando novos produtos,
#então o programa deve permitir e entrada de quantos produtos o usuário quiser.

venda = input('registre um produto. Para cancelar clique enter: ')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input('registre um produto. Para cancelar clique enter: ')

print(f'cadastro finalizado. Os produtos cadastrados foram: {vendas}')