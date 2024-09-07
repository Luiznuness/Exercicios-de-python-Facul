"""

14 – Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que
o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma
e a média aritmética. 

"""

def loop():
    lista = list()
    
    print('Para você sair do programa é só digitar o número 0')
    valor = int(input('Digite um número: '))
    
    lista.append(valor)

    while valor != 0:
        valor = int(input('Digite um número: '))
        if valor != 0:
            lista.append(valor)
    
    soma = 0
    
    for vezes in lista:
        soma += vezes
    
    media = soma / len(lista)

    print(f'A soma dos números que foram digitados é: {soma}')
    print(f'A média dos números que foram digitados é: {media:.2f}')


if "__main__" == __name__:
    loop()