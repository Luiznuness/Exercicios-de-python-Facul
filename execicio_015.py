"""

15 – Escreva um programa para controlar uma pequena maquina registradora. Você solicita o usuário que
digite o código do produto e a quantidade comprada. Utilize a tabela de código a seguir para obter o preço
de cada produtor.

• Código 1 – Preço R$ 0,50
• Código 2 – Preço R$ 1,00
• Código 4 – Preço R$ 4,00
• Código 5 – Preço R$ 7,00
• Código 9 – Preço R$ 8,00

Seu programa deve exibir o total das compras depois que o usuário digitar 0. Quaisquer outros códigos
devem gerar a mensagem de erro “Código Invalido”.

"""

def codigos():
    print()
    print('Código 1 – Preço R$ 0,50')
    print('Código 2 – Preço R$ 1,00')
    print('Código 4 – Preço R$ 4,00')
    print('Código 5 – Preço R$ 7,00')
    print('Código 9 – Preço R$ 8,00')
    print()

def loop():
    codigo = 1

    total = 0

    print('Você está em uma maquina registradora, se você quiser sair é só você digitar o número 0')
    
    while codigo != 0:
        codigo = int(input('Digite o código do produto:\n'))
        
        if codigo == 1:
            quant = int(input('Quantos produtos desses você tem ai ?\n'))
            soma = 0.50 * quant
            total+=soma

        elif codigo == 2:
            quant = int(input('Quantos produtos desses você tem ai ?\n'))
            soma = 1 * quant
            total+=soma

        elif codigo == 4:
            quant = int(input('Quantos produtos desses você tem ai ?\n'))
            soma = 4 * quant
            total+=soma

        elif codigo == 5:
            quant = int(input('Quantos produtos desses você tem ai ?\n'))
            soma = 7 * quant
            total+=soma
        
        elif codigo == 9:
            quant = int(input('Quantos produtos desses você tem ai ?\n'))
            soma = 8 * quant
            total+=soma
        elif codigo == 0:
            print('Você acabou de fazer todas as suas compras')
            if type(total) == float:
                print()
                print(f'Deu R${total:.2f}, Qual seria a forma de pagamento ? ;)')
            else:
                print()
                print(f'Deu R${total}, Qual seria a forma de pagamento ? ;)')
        else:
            print('CÓDIGO INVALIDO BOCA ABERTA')
            print('Os códigos são:')
            codigos()

    return total



if "__main__" == __name__:
    loop()