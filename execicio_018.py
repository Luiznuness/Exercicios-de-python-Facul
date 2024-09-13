"""

18 – Modifique o programa da questão 16 para trabalhar com nota de R$ 100,00.

"""

def banco(valor):
    
    valores = {"100": 0, "50": 0, "20": 0, "10": 0, "4": 0, "1": 0}

    if valor == 0:
        print('Você é burro né ?')
        print(f'Como você vai sacar R${valor}')
    else:
        while valor != 0:
            if valor >= 100:
                valor-=100
                valores['100']+=1
            
            elif valor >= 50:
                valor-=50
                valores['50']+=1
            
            elif valor >= 20:
                valor-=20
                valores['20']+=1
            
            elif valor >= 10:
                valor-=10
                valores['10']+=1
            
            elif valor >= 4:
                valor-=4
                valores['4']+=1
            
            elif valor >= 1:
                valor-=1
                valores['1']+=1

            else:
                print("Esse valor nós não temos, sinto muito !!")
    
    for vezes, valores in valores.items():
        if valores != 0:
            print(f'Você acabou de sacar {valores} notas de {vezes} !')          

if "__main__" == __name__:
    valor = int(input('Qual valor você deseja sacar ?\n'))
    banco(valor=valor)