"""

18 – Modifique o programa da questão 16 para trabalhar com nota de R$ 100,00.

"""

def banco(valor):
    cedula100 = 0
    cedula50 = 0
    cedula20 = 0
    cedula10 = 0
    cedula4 = 0
    cedula1 = 0

    if valor == 0:
        print('Você é burro né ?')
        print(f'Como você vai sacar R${valor}')
    else:
        while valor != 0:
            if valor >= 100:
                valor-=100
                cedula100+=1
            
            elif valor >= 50:
                valor-=50
                cedula50+=1
            
            elif valor >= 20:
                valor-=20
                cedula20+=1
            
            elif valor >= 10:
                valor-=10
                cedula10+=1
            
            elif valor >= 4:
                valor-=4
                cedula4+=1
            
            elif valor >= 1:
                valor-=1
                cedula1+=1
            
            else:
                print()

        if cedula100 != 0:
            print(f'Você sacou {cedula100} cédulas de R$100,00') 

        if cedula50 != 0:
            print(f'Você sacou {cedula50} cédulas de R$50,00')

        if cedula20 != 0:
            print(f'Você sacou {cedula20} cédulas de R$20,00')

        if cedula10 != 0:
            print(f'Você sacou {cedula10} cédulas de R$10,00')

        if cedula4 != 0:
            print(f'Você sacou {cedula4} cédulas de R$4,00')

        if cedula1 != 0:
            print(f'Você sacou {cedula1} cédulas de R$1,00')      

if "__main__" == __name__:
    valor = int(input('Qual valor você deseja sacar ?\n'))
    banco(valor=valor)