
#enumetare permite que voce percorra uma lista e ao mesmo tempo tenha em uma variavel o indice daquela lista

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
for funcionario in funcionarios:
    print(funcionario)


for i, funcionario in enumerate(funcionarios):
    print(f'{i} : {funcionario}')




#Em uma fábrica você tem vários produtos e não pode deixar que os produtos fiquem em falta.
#Para isso, foi definido uma quantidade mínima de estoque que os produtos precisam ter:
#Identifique quais produtos estão abaixo do nível mínimo de estoque.


estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50

for i, produto in enumerate(produtos):
    if estoque[i] < nivel_minimo:
        print(f'produto n° {i} esta em falta no estoque com apenas {estoque[i]} produtos: {produto}')