'''
Estrutura:
dicionario = {chave: valor, chave: valor, ...}

Vantagens e Desvantagens

- Não devem ser usados para pegar itens em uma determinada ordem
- Podem ter valores heterogêneos (vários tipos de valores dentro de um mesmo dicionário: inteiros, strings, listas, etc)
- Chaves são únicas obrigatoriamente
- Mais intuitivos de trabalhar
'''

mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

#- Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?

livroMaisVendido = mais_vendidos['livros']
print(f'o livro mais vendido é {livroMaisVendido}')

lazerMaisVendido = mais_vendidos['lazer']
print(f'o lazer mais vendido foi {lazerMaisVendido}')


#- Quanto foi vendido de 'notebook asus' e de 'ipad'?

vendasNotebookAsus = vendas_tecnologia['notebook asus']
print(f'foram vendidos {vendasNotebookAsus} notebook asus')

vendaIpad = vendas_tecnologia['ipad']
print(f'foram vendidos {vendaIpad} ipad')