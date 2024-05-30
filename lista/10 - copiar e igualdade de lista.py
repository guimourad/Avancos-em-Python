#copiar e igualdade de lista

#isso faz com que eu possa copiar a lista e modificar apenas uma sem afetar a outra



apple = ["ipad", 'iphone', 'apple tv']
appleCopia = apple
itensApple = apple.copy()



apple[1] = 'iphone 15' 

print(apple)
print(appleCopia)
print(itensApple)

#modifiquei uma lista, a copia dela permaneceu como antes e a que apenas criei a variavel (appleCopia) modificou tambem