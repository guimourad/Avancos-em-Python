'''
# List Comprehension com if para escolher o resultado final

### Estrutura:
lista = [item if condicao else outro_resultado for item in iterable]
'''

#- Digamos que eu esteja analisando os vendedores de uma loja e 
# queira criar uma lista para enviar para o RH com o bônus de cada vendedor.
#- O bônus é dado por 10% do valor de vendas dele, caso ele tenha batido a meta

vendedores_dic = {'Maria': 1200, 'José': 300, 'Antônio': 800, 'João': 1500, 'Francisco': 1900, 'Ana': 2750, 'Luiz': 400, 'Paulo': 20, 'Carlos': 23, 'Manoel': 70, 'Pedro': 90, 'Francisca': 80, 'Marcos': 1100, 'Raimundo': 999, 'Sebastião': 900, 'Antônia': 880, 'Marcelo': 870, 'Jorge': 50, 'Márcia': 1111, 'Geraldo': 120, 'Adriana': 300, 'Sandra': 450, 'Luis': 800}
meta = 1000

#for
bonus = []
for item in vendedores_dic:
    if vendedores_dic[item] > meta:
        bonus.append(vendedores_dic[item] *0.1)
    else: bonus.append(0)

print(bonus)

#list comprehension
bonus = [vendedores_dic[item] * 0.1 if vendedores_dic[item] > meta else 0 for item in vendedores_dic ]
print(bonus)