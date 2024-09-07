"""

08 – Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo
segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender a multiplicação de dois números como a soma sucessivas de um deles. Assim, 4 x 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

"""

valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))

soma = valor1

for c in range(1, valor2):
    soma+=valor1
print(f'A multiplicação entre o número {valor1} e o número {valor2} é igual a {soma}')