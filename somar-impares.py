import os

LOOP_MAXIMO = 3
    
def mostrar_titulo(loop_maximo):
    print('Bem-vindo(a) ao programa!')
    print('-' * 60)
    print(f'Contador de {loop_maximo} números ímpares\n')
    

def ler_numeros(loop_maximo):
    numeros = []
    for i in range(1, loop_maximo + 1):
        while True:
            try:
                numero = int(input(f'{i}) Digite um número: '))
                numeros.append(numero)
                break
            except ValueError:
                print('Digite um valor inteiro!')
    return numeros

def somar_impares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 != 0:
            soma += numero
    return soma

def exibir_resultado(soma):
    os.system('cls')
    print(f'A soma total dos números ímpares: {soma}')

def main():
    mostrar_titulo(LOOP_MAXIMO)
    numeros = ler_numeros(LOOP_MAXIMO)
    soma = somar_impares(numeros)
    exibir_resultado(soma)
    
if __name__ == '__main__':
    main()
