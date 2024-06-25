'''
# Ordem dos Argumentos

### Estrutura:

- Sempre os positional arguments vêm antes e depois os keywords arguments.
- Sempre os argumentos individuais vêm antes e depois os "múltiplos"
'''

#def minha_funcao(arg1, arg2, arg3, arg4, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs):

#def mSoma(num1, *numeros):
#or
def mSoma(*numeros, num1):
    soma = 0
    for numero in numeros:
        soma += numero
    soma += num1
    return soma

#print(mSoma(1, 2, 3 , 4))
#or
print(mSoma(1, 2, 3 ,num1= 4))
