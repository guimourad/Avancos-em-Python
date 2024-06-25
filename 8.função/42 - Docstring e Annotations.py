'''
# Docstring e Annotations

Estrutura - São ferramentas "apenas" para organização:

Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função
e também pode ser que a gente precise usar essa mesma função semanas, meses ou até anos depois da sua criação.

Por isso é importante usarmos DocStrings e Annotations

- Docstring -> diz o que a função faz, quais valores ela tem como argumento e o que significa cada valor
- Annotation -> diz o que devem ser os argumentos e o que a função retorna

Em muitas empresas, o time de tecnologia vai ter um padrão que você deve seguir para isso,
mas caso não tenha, vamos te mostrar um padrão bom a ser utilizado.
'''

# Docstring:
def minha_funcao(arg1, arg2):
    '''O que a função faz
    
    Parameters:
        arg1 (int): o que é o argumento 1
        arg2 (str): o que é o argumento 2
        ...
    
    Returns:
        texto (str): o que a função retorna como resposta
    '''


# Annotation
'''
def minha_funcao(arg1: isso, arg2: aquilo) -> o que a função retorna:
    ...
    return ...


def minha_soma(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3
'''