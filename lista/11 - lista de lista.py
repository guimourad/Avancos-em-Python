#lista de lista

vendedores = ['guilherme', 'thiago', 'eleide', 'samir']
produtos = ['apple watch', 'airpods']
vendas = [
    [150, 200],
    [250, 300],
    [350, 400],
    [450, 500],
]

#quanto guilherme vendeu de airpods

vendasAirpodsGuilherme = vendas[0][1]
print(vendasAirpodsGuilherme)

#quanto eleide vendeu de apple watch

vendasApplewatchEleide = vendas[2][0]
print(vendasApplewatchEleide)

#qual total de vendas de airpods

a = vendas[0][1]
b = vendas[1][1]
c = vendas[2][1]
d = vendas[3][1]


vendasAirpods = a + b + c + d
print(vendasAirpods)


#se guilherme fez na verdade 100 vendas de apple watch, como modificar na lista o valor da venda

vendas[0][0] = 100
print(vendas)

# se eu tenho um novo produto 'mac', como adicionar as vendas de cada vendedor

vendasMac = [1000, 1500, 1750, 1875]

vendas[0].append(vendasMac[0])
vendas[1].append(vendasMac[1])
vendas[2].append(vendasMac[2])
vendas[3].append(vendasMac[3])

print(vendas)