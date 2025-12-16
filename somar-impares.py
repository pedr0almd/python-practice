# Status: Não concluído
numeros = []
numero = 0
soma = 0
    
def mostrar_titulo():
    print('Bem-vindo(a) ao programa!')
    print('-' * 60)
    print('Contador de números ímpares\n')
    

def ler_numeros():
    for i in range(1, 4, 1):
        numero = int(input(f'{i}) Digite um número: '))
        numeros.append(numero)

def somar_impares(soma):
    for numero in numeros:
        if numero % 2 == 1:
            soma += numero
    print(soma)


mostrar_titulo()
ler_numeros()
somar_impares(soma)
