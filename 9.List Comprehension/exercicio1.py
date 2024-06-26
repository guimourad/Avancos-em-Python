'''
# Exercícios

## 1. Tirando informações de listas e dicionários

Digamos que você está analisando as vendas de produtos de uma empresa de varejo.

Essa lista tem: (produto, vendas de 2019, vendas de 2020) para cada produto.

Crie uma lista com as vendas de 2019.
'''

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]
'''
listaVendas2019 = []
for produto, venda2019, venda2020 in vendas_produtos:
    listaVendas2019.append(venda2019)
print(listaVendas2019)
'''
vendas2019 = [venda2019 for produtos, venda2019, venda2020 in vendas_produtos]
print(vendas2019)


#- Agora, qual o maior valor de vendas de 2019?

maior = max(vendas2019)
print(f'maior venda de 2019 foi {maior}')

#- E se eu quisesse descobrir o produto que mais vendeu em 2019?
#Temos 2 formas de fazer, refazendo o list comprehension ou consultando a lista original
produtoMaisVendido2019 = [(venda2019, produtos ) for produtos, venda2019, venda2020 in vendas_produtos]
print(max(produtoMaisVendido2019))
