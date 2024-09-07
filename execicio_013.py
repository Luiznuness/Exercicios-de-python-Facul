"""

13 – Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal. Pergunte também o
valor mensal que será pago. Imprima o número de meses para que a divida seja paga, o total pago e o total
de juros pago.

"""

divida = float(input("Qual o valor da divida ?\n")) # Valor total sem juros

juros = float(input("Qual a porcentagem de juros por mês ?\n")) # Valor total a ser calculado

pagar_mes = float(input('Qual o valor a ser pago por mês ?\n')) # Valor que será pago todo o mês até que a divida seja sanada

contador = 0 # Contara a quantidade de Mês que foram precisos para sanar a divida

total_juros = 0 

total_pago = 0

while divida != 0:
    if divida < pagar_mes:
        pagar_mes = divida
        divida -= pagar_mes # Tirando o que foi pago no mês do valor dá divida
        print(f"No ultimo mês só foi preciso pagar {pagar_mes:.2f}")
    else:
        divida -= pagar_mes

    total_pago += pagar_mes

    valor_juros = (divida*juros) / 100 # Calculando o juros com base no valor da divida

    total_juros += valor_juros

    divida += valor_juros # Somando o valor da divida mais os juros do mês 

    contador += 1 # Contando o mês

print(f'Foram necessarios {contador} meses para sanar a divida')
print(f'Foram pagos R${total_juros:.2f} em juros')
print(f'Foram pagos R${total_pago:.2f} em toda divida')