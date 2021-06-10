import random

#lowerCase = 'abcdefghijklmnopqrstuvwxyz'
#upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#numeros = '0123456789'
#simbolos = '!@#$%¨&*(){}[],.;:'

#tudo = lowerCase + upperCase + numeros + simbolos
#semSimbolo = lowerCase + upperCase + numeros

tudo = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*(){}[]'
semSimbolo = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
soNumero = '0123456789'
#caracteresEspeciais = '!@#$%¨&*(){}[]'

#print("Digite Quantos Caracteres a Senha Terá: ")
selecao = ''
selecao = int(input("Digite Quantos Caracteres a Senha Terá: "))
senha= ''

escolha = int(input("\nQual o Tipo de Senha que Deseja?\n1 - Tudo(Símbolos, Letras e Números)\n2 - Apenas Letras e Números\n3 - Apenas números:\n"))

if(escolha == 1):    
    for i in range(selecao):
#        next_index = random.randrange(len(tudo))
#        senha = senha + tudo[next_index]
        senha += random.choice(tudo)
    print("\nSenha:", senha)

elif(escolha == 2):
    for i in range(selecao):
#        next_index = random.randrange(len(semSimbolo))
#        senha = senha + tudo[next_index]
        senha += random.choice(semSimbolo)
    print("\nSenha:", senha)

elif(escolha == 3):
    for i in range(selecao):
#        next_index = random.randrange(len(semSimbolo))
#        senha = senha + tudo[next_index]
        senha += random.choice(soNumero)
    print("\nSenha:", senha)

else:
    print("Essa escolha NÃO EXISTE!\nREINICIE O PROGRAMA E ESCOLHA ENTRE 1, 2 e 3 SEU ANIMAL")

input("")
