import os

numeros = []

def limpar_tela():
    os.system('cls')

def ler_numero():
    for _ in range(0, 10, 1):
        limpar_tela()
        try:
            numero = int(input('Digite um número: '))
            numeros.append(numero)
        except:
            print('Digite um número inteiro válido!')
        
def somar_numeros():
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

def fazer_divisao():
    try:
        soma = somar_numeros()
        return soma / len(numeros)
    except ZeroDivisionError:
        return 'Não é possível dividir por zero.'

def mostrar_mensagem():
    print(fazer_divisao())
        
ler_numero()
mostrar_mensagem()

 
