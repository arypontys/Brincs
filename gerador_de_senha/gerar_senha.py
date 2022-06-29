# Gerador de senhas aleatórias
import random

def gerar_senha():
    '''
    Gerar senhas aleatórias com 12 caracteres

    alfabeto: caracteres do alfabeto
    numeros: numeros de 0 a 9
    simbolos: 10 síbolos especiais
    lista senha: variável que recebe os caracteres ramdomizados na sequencia das variáveis dispostas
    senha: variável que recebe os caracteres já tratados e aleatorios. 
    '''

    alfabeto = ['q','w','e','r','t','y','u','i','o','p','a','s','d',
    'f','g','h','j','k','l','ç','z','x','c','v','b','n','m','Q',
    'W','E','R','T','Y','U','I','O','P','A','S','D','F','G',
    'H','J','K','L','Ç','Z','X','C','V','B','N','M']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    simbolos = ['!','@','#','$','%','&','*','(',')','+']
    lista_senha =[]
    senha = []
    
    for l in range(0, 8):
        lista_senha.append(random.choices(alfabeto))
    for l in range(0, 2):
        lista_senha.append(random.choices(numeros))
    for l in range(0, 2):
        lista_senha.append(random.choices(simbolos))
    
    random.shuffle(lista_senha)

    for l in lista_senha:
        for i in l:
            senha.append(i)
        a = ''.join(senha)

    return a

senha = gerar_senha()
print(senha)