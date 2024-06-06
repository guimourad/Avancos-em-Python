def imprimirLinha():
    print("-" * 20)


#Alterações Incrementais de Variáveis (Importante)

faturamento = 5000
faturamento = faturamento + 2500
print(faturamento)

email = 'guimourad@gmail'
email = email + '.com'
print(email)

imprimirLinha()

listaP = ['mac', 'iphone']
listaV = [1500, 2250]
#adicionar ipad na lista
#pode usar o append tambem
listaP = listaP + ['ipad']
print(listaP)

imprimirLinha()
#adicionando na soma a quantidade de ipad
somaVendaIpad = 3750
somaVendaIpad += 2800
print(somaVendaIpad)

email = f'Esse mes vendemos um total de {somaVendaIpad} produtos, sendo:\n{listaV[0]} unidades de {listaP[0]}\n{listaV[1]} unidades de {listaP[1]}'
#adicionando no fim do texto o ipad

email = email + f'\n{2800} unidades de ipad'
print(email)