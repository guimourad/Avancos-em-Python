'''
# Exceções e Erros em Funções

 Como "testar" erros e tratar exceções:

 try:
    o que eu quero tentar fazer
except:
    o que vou fazer caso dê erro
'''


def descobrirServidor(email):
    try:
        pocisaoA = email.index('@')
    except:
        raise Exception('email digitado nao tem @, tente novamente')
    else:
        servidor = email[pocisaoA:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'oul' in servidor:
            return 'uol'
        else:
            return 'nao determinado'
#desse jeito, eu isolo o erro, nesse caso de ser digitado um email sem @


    
email = input('qual o seu email? ')
print(descobrirServidor(email))


#- Cuidado: uma vez dentro do try, qualquer erro vai levar ao except

### Como "printar" um erro em uma function
'''
raise Exception('O erro foi esse')

ou então avisando qual o tipo de erro que ele teve

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse')
'''

### Tratamento Completo:

'''
try:
    tente fazer isso
except ErroEspecífico:
    deu esse erro aqui que era esperado 
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.
'''