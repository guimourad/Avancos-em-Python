'''
Antes de irmos para o desafio que apresentamos na última aula 
(que é bem mais complexo do que um exemplo simples) 
vamos resolver um exercício um pouco mais simples para treinar

## 1. Cálculo do Percentual e da Lista de Vendedores

- Queremos criar uma function que consiga identificar os vendedores que bateram uma meta,
mas além disso, consigo já me dar como resposta o cálculo do % da lista de vendedores
que bateu a meta (para eu não precisar calcular manualmente depois)
- Essa function deve receber 2 informações como parâmetro:
a meta e um dicionário com os vendedores e suas vendas. E me dar 2 respostas:
uma lista com o nome dos vendedores que bateram a meta e o % de vendedores que bateu a meta.
'''

meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def calculoMeta(meta, vendas):
    bateuMeta = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            bateuMeta.append(vendedor)
    percentualBateuMeta = len(bateuMeta) / len(vendas)
    return percentualBateuMeta, bateuMeta


#print(calculoMeta(meta, vendas))

#podemos fazer o unpacking
percentualMeta, vendedoresAcima = calculoMeta(meta, vendas)
print(percentualMeta)
print(vendedoresAcima) 