"""

11 – Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança. Exiba os
valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

"""

valor_inicial = float(input('Qual seria o seu primeiro deposito ?\n'))

imposto = float(input('Quantos porcento seu dinheito renderá por mês ?\n'))

valor_atual = valor_inicial

for vezes in range(1, 25):
    com_impostos = ((imposto * valor_atual) / 100) + valor_atual
    print(f'No {vezes}° mês vocês estará com R${com_impostos:.2f}')
    valor_atual = com_impostos

total_ganho = valor_atual - valor_inicial

if '0' in str(imposto):
    print(f'\nNo final dos 2 anos e o seu dinheito rendendo {int(imposto)}% por mês você terá um total de {total_ganho:.2f} de ganhos')
else:
    print(f'\nNo final dos 2 anos e o seu dinheito rendendo {imposto}% por mês você terá um total de R${total_ganho:.2f} de ganhos')