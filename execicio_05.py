"""

05 – Escreva um programa que mostre os números de 1 até o numero digitado pelo usuário, mas, apenas
os números múltiplos de 3. 

"""

valor_final = int(input('Digite até quanto você quer contar: '))

for vezes in range(1, valor_final+1):
    if vezes%3 == 0:
        print(vezes)