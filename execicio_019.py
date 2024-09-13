"""

19 – Modifique o programa da questão 16 para aceitar valores decimais, ou seja, também contar moedas de
R$0.01, R$0.02, R$0.05, R$0.10, e R$0.50.

"""

def saque_reais(valor):
    reais = {"100": 0, "50": 0, "20": 0, "10": 0, "4": 0, "1": 0}

    if valor == 0:
        print('Você é burro né ?')
        print(f'Como você vai sacar R${valor}')
    else:
        while valor != 0:
            if valor >= 100:
                valor-=100
                reais['100']+=1
            
            elif valor >= 50:
                valor-=50
                reais['50']+=1
            
            elif valor >= 20:
                valor-=20
                reais['20']+=1
            
            elif valor >= 10:
                valor-=10
                reais['10']+=1
            
            elif valor >= 4:
                valor-=4
                reais['4']+=1
            
            elif valor >= 1:
                valor-=1
                reais['1']+=1
            else:
                if valor < 1 and valor > 0:
                    valor = round(valor, 2)
                    valor = saque_centavos(valor)
                else:
                    print("Esse valor nós não temos, sinto muito !!")
                    break    

    for vezes, valores in reais.items():
        if valores != 0:
            print(f'Você acabou de sacar {valores} notas de {vezes} !')

def saque_centavos(valor):
    centavos = {"0.01": 0, "0.02": 0, "0.05": 0, "0.10": 0, "0.50": 0}

    if valor == 0:
        print('Você é burro né ?')
        print(f'Como você vai sacar R${valor}')
    else:
        while valor != 0:     
       
            valor = round(valor, 2)
            
            if valor >= 0.50:
                valor-=0.50
                centavos['0.50']+=1

            elif valor >= 0.10:
                valor-=0.10
                centavos['0.10']+=1

            elif valor >= 0.05:
                valor-=0.05
                centavos['0.05']+=1

            elif valor >= 0.02:
                valor-=0.02
                centavos['0.02']+=1

            elif valor >= 0.01:
                valor-=0.01
                centavos['0.01']+=1
            else:
                print("Esse valor nós não temos, sinto muito !!")
                return valor
    

    for vezes, valores in centavos.items():
        if valores != 0:
            print(f'Você acabou de sacar {valores} moedas de {vezes} !')
    return valor
    
    
            
def banco(valor):   
    saque_reais(valor)

if "__main__" == __name__:
    valor = float(input('Qual valor você deseja sacar ?\n'))
    banco(valor=valor)