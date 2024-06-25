'''
- Vamos criar uma function com parâmetro

Digamos que estamos criando um programa para categorizar os produtos de uma revendedora de bebidas.

Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.

Ex:
Vinho -> BEB12302<br>
Cerveja -> BEB12043<br>
Vodka -> BEB34501<br>

Guaraná -> BSA11104<br>
Coca -> BSA54301<br>
Sprite -> BSA34012<br>
Água -> BSA09871<br>

Repare que bebidas não alcóolicas começam com BSA e bebidas alcoolicas começam com BEB.

Crie um programa que analise uma lista de produtos 
e envie instruções para a equipe de estoque dizendo quais produtos devem ser enviados para
a área de bebidas alcóolicas.
'''


produtos = ['BEB46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

#percorrer a lista de produtos
#verificar cada produto se é bebiba alcoolica
#se a resposta for sim, printar o produto 

def ehAlcolico(bebida):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False


for produto in produtos:
    if ehAlcolico(produto):
        print(f'O produto {produto} deve ser enviado para a área de bebidas alcóolica')
    