### Forma de pensar

# Top -> Down
    # dividir o problema em etapas para facilitar a construção do codigo

# Exemplo simples: atravessar a rua
    #olhar para os dois lados
        #olhar para a direita e ver se esta vindo carro
        #se sim, esperar que o carro passe
        #se nao, olhar para a esquerda e ver se esta vindo carro
        #se sim, esperar que o carro passe
    # atravesar ate o outro lado da calçada 


### Exemplo de Exercício do Curso
'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, 
que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.
'''

'''
##### Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.

Dica: lembre dos operadores // e % mostrados em exercícios anteriores
Dica: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10. Ex: 7 // 3 = 2; 10 // 3 = 3
Dica: numero % 10 vai te dar o resto da divisão do número por 10. Ex: 7 % 3 = 1; 10 % 3 = 1; 15 % 3 = 0
'''
##### 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)

#descobrir quantas latas de tinta e qual o custo para pintar uma area
    #descobrir quantas latas de tinta
        #descobrir a area que vai ser pintada
area = int(input('qual a area que vai ser pintada (m²): '))

        #quantos litros de tinta vou precisar para essa area
litros = area / 6

        #quantas latas vou precisar para pintar essa area
latas = litros / 18

##-> se a quantidade de latas for maior que um numero inteiro, comprar uma lata a mais
if latas > int(latas):
    latas =  int(latas) + 1 
    
    #calcular o custo total da tinta
        #quantidade de lata * preco da lata
preco = latas * 80

print(f'latas: {latas}')
print(f'preco {preco}')


