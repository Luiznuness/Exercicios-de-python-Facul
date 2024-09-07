"""

12 – Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor
será depositado no inicio de cada mês, e você deve considera-lo para o calculo de juros do mês seguinte.

"""

valor_inicial = float(input('Qual seria o seu primeiro deposito ?\n'))

imposto = float(input('Quantos porcento seu dinheito renderá por mês ?\n'))

valor_mes = float(input('Qual valor vai ser adicionado no começo dos mêses ?\n'))

valor_atual = valor_inicial

print(f'No inicio da economia você tem R${valor_atual:.2f}')

for vezes in range(1, 25):
    if vezes > 1:
        com_impostos = ((imposto * valor_atual) / 100) + valor_atual + valor_mes
    else:
        com_impostos = ((imposto * valor_atual) / 100) + valor_atual

    print(f'No {vezes}° mês vocês estará com R${com_impostos:.2f}')
    valor_atual = com_impostos

total_ganho = (valor_atual - valor_inicial) - (valor_mes * 23)

if '0' in str(imposto):
    print(f'\nNo final dos 2 anos e o seu dinheito rendendo {int(imposto)}% por mês você terá um total de {total_ganho:.2f} de ganhos')
else:
    print(f'\nNo final dos 2 anos e o seu dinheito rendendo {imposto}% por mês você terá um total de R${total_ganho:.2f} de ganhos')