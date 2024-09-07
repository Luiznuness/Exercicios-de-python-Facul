"""

04 – Escreva um programa que mostre os números de 1 até um numero digitado pelo usuário, mas, apenas
os números impares.

"""

solicitado = int(input('Digite um número: '))

for valor in range(0, solicitado):
    impar = valor%2

    if impar == 1:
        print(valor)
