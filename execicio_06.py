"""

06 – Escreva um programa que exiba a tabuada do número digitado de 0 a 10.

"""

valor = int(input('Digite um valor: '))

for vezes in range(0, 11):
    print(f'{valor} x {vezes} = {valor*vezes}')