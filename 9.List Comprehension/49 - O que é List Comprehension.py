'''
# List Comprehension - O que é e qual a importância?

### Descrição:

- List Comprehension é uma forma de iterar pelos elementas das listas de maneira "mais direta",
 com mais "cara de Python"
- Em resumo: é como se você fizesse um "for" em 1 linha de código

### Observação Importante:

- Você não precisa de List comprehension para programar, 
tudo que vamos mostrar aqui dá pra fazer do jeito que já aprendemos
- Você não vai sair de uma hora pra outra fazendo tudo list comprehension ao invés de for,
porque é realmente mais confuso.
- O objetivo aqui é:
    1. Saber ler e entender o que tá acontecendo quando ver list comprehension (principal)
    2. A medida do tempo você vai se acostumando com isso, vendo mais,
    usando mais e vai fazer naturalmente quando precisar.
    
- Mas se você sair desse módulo do curso achando isso tudo muito difícil, fica tranquilo,
não usa por hora list comprehension e a medida que você for pegando 
mais experiência com o Python você lembra que tem esse módulo aqui e pode voltar no futuro

### Estrutura:

lista = [expressão for item in iterable]
'''


preco_produtos = [100, 150, 300, 5500]
produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']

#digamos que o imposto sobre os produtos é de 30%, ou seja, 0.3. Como eu faria para criar uma lista com os 
#valores de imposto de cada produto?

#usando for
imposto = []
for preco in preco_produtos:
    imposto.append(preco * 0.3)
print(imposto)


#Usando list comprehension
imposto = [preco * 0.3 for preco in preco_produtos]
# imposto é uma lista onde cada item é o preco * 0.3 para cada preco dentro da lista preco_produtos
print(imposto)


# A "expressão" na list comprehension pode ser uma function tb
def calcular_imposto(preco, imposto):
    return preco * imposto

imposto = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
#para cada preco dentro da minha lista de preco o item do meu imposto vai ser o resultado da funcao (preco e 0.3) 
print(imposto)


'''
### Observação:

- Normalmente isso é usado quando queremos fazer uma única ação com os itens de uma lista.
Não é obrigatório, mas é comum de encontrar principalmente com programadores
mais experientes/preocupados com "a melhor forma de fazer alguma coisa"

- Cuidado: se a sua lista for MUITO grande, o list comprehension pode acabar sendo difícil de compilar.
Nesses casos podemos usar funções, for tradicionais com breaks para interromper
ou até bibliotecas como o panda que trabalham bem com muitos dados
'''
