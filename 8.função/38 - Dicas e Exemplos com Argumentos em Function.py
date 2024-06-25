'''
Exemplos de parâmetros


- upper() -> não tem parâmetros 
- sort() -> apenas parâmetros keyword
- extend(lista) -> 1 parâmetro obrigatório
- nossa função eh_da_categoria(bebida, cod_categoria) -> 2 parâmetros de posição obrigatórios
'''

def ehDaCategoria(bebida, codCategoria):
    bebida = bebida.upper()
    if codCategoria in bebida:
        return True
    else:
        return False
    
codProduto = 'beb1234'
print(codProduto.upper()) #-> tudo maiusculo

vendasAno = [50, 30, 10, 70, 60, 50, 40, 20]
novasVendas = [100, 120]

print(vendasAno.sort()) #-> ordena em ordem crescente

vendasAno.extend(novasVendas)
print(vendasAno)