"""

09 – Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim
como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembrese de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que
podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de
20.

"""

valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))

if valor1 > valor2:
    sub = valor1
    div = 1

    while valor2 < sub:
        div+=1
        sub-=valor2

    if sub == 0:
        print(div)
    else:
        print('A divisão não dara um número inteiro')
        print(f'O resto da divisão é: {sub}')
else:
    print("Desse jeito a divisão não dará um número inteiro, tente novamente!!!")