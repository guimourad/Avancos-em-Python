'''
# Mais sobre o return

Pontos importantes:

- Podemos usar no return praticamente qualquer tipo de objeto:
(número, string, lista, tupla, dicionário, outros objetos, etc.)
- O return, se for executado, encerra a função, mesmo que dentro dela haja um loop.
'''

#retornar um numero
def numero (num1, num2, num3):
    return num1+num2+num3

#retornar um texto
def padraoTexto(texto):
    texto = texto.casefold()
    texto = texto.replace('  ', ' ')
    texto = texto.strip()
    return texto

#retornar um boolean
def bateuMeta(vendas, meta):
    if vendas > meta:
        return True
    else:
        return False
    
#retornar lista, tupla ou dicionario
def filtarListaTexto(lista, pedacoTexto):
    listaFiltrada = []
    for item in lista:
        if pedacoTexto in item:
            listaFiltrada.append(item)
    return listaFiltrada
    


vendasGuilherme = 200
meta = 180

if bateuMeta(vendasGuilherme, meta):
    print('bati a meta')


listaTexto = ['hashtag@gmail.com', 'gui@gmail.com', 'lira@hotmail.com', 'bitriz@hotmail.com']
listaA = filtarListaTexto(listaTexto, 'gmail')
print(listaA)


