"""

07 – Escreva um programa que exiba a tabuada do número digitado, onde o usuário possa escolher o inicio
e o fim da tabuada. 

"""

valor = int(input('Digite o número da tabuada: '))
inicio = int(input('Onde começa: '))
fim = int(input('Onde termina: '))

if fim < inicio:
    print('O primeiro número tem que ser maior que o segundo!!!!!!!!')
    while fim < inicio:
        inicio = int(input('Onde começa: '))
        fim = int(input('Onde termina: '))
        for vezes in range(inicio, fim+1):
            print(f'{valor} x {vezes} = {valor*vezes}')
else:
    for vezes in range(inicio, fim+1):
            print(f'{valor} x {vezes} = {valor*vezes}')