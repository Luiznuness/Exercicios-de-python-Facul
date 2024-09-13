"""

21 – Reescreva o programa da questão 16 de forma a continuar executando até que o valor digitado seja 0.
Utilize repetições aninhadas.

"""

from execicio_019 import banco

def ex_16_refresh():
    print()
    print('Você está prestes a entrar em um programa de saque de dinhero !!')
    print('Quando você quiser sair do programa é só digitar o número 0')
    print()

    valor = float(input("Digite o valor que vc deseja sacar: "))
    banco(valor=valor)

    while valor != 0:
        valor = float(input("Digite o valor que vc deseja sacar: "))
        banco(valor=valor)


if "__main__" == __name__:
    ex_16_refresh()

    # Eu preciso arrumar um jeito de quando eu passar o valor 10.10 para a minha função, ela conseguir fazer os saque da forma correta.
    # Pq quando eu faço isso e eu tira 10 de 10.10, eu não consigo pegar os 0.10 que restaram, ele me retorna 0.0999...
    # A perguta certa é: Como eu faço para tirar somente o valor inteiro de um float, ou como eu tiro somente o valor depois do ponto de um float
    # Espere as cenas dos próximos capitulos 