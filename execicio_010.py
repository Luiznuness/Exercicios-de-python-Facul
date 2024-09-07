"""

10 – Escreva um programa que corrija um teste de múltiplas escolhas de três questões. A resposta da
primeira questão é “b”; da segunda, “a”; e da terceira, “d”. O programa conta um ponto a cada
resposta correta. Considere a possibilidade do programa aceitar respostas com letra maiúsculas e minúsculas
em todas as questões

"""
def questoes():
    acertos = 0
    lista = []
    print('1. O que a função len() faz em Python?')
    print('a) Retorna a soma dos elementos de uma lista')
    print('b) Retorna o número de elementos em um objeto')
    print('c) Concatena duas listas')
    print('d) Remove o último elemento de uma lista')
    quest1 = input().upper()[0] # Resposta = b
    print('2. Qual das seguintes opções define uma tupla em Python?')
    print('a) tupla = [1, 2, 3]')
    print('c) tupla = (1, 2, 3)')
    print('b) tupla = {1, 2, 3}')
    print('d) tupla = <1, 2, 3>')
    quest2 = input().upper()[0] # Resposta = a
    print('3. Qual função em Python converte um valor para um número inteiro?')
    print('a) str()')
    print('b) float()')
    print('c) bool()')
    print('d) int()')
    quest3 = input().upper()[0] # Resposta = d

    if quest1 == 'B':
        lista.append(True)
        acertos+=1
    else:
        lista.append(False)
    
    if quest2 == 'A':
        acertos+=1
        lista.append(True)
    else:
        lista.append(False)
    
    if quest3 == 'D':
        lista.append(True)
        acertos+=1
    else:
        lista.append(False)
    print(f'Você acertou {acertos} questões')
    return lista

if "__main__" == __name__:
    fazer = 'S'

    while fazer == 'S':
        result = questoes()

        for vezes, valor in enumerate(result):
            if valor:
                print(f'Você acertou a questão: {vezes+1}')
            else:
                print(f'Você errou a questão: {vezes+1}')
        fazer = input('\nVocê quer refazer o teste ? [Sim / Não]\n').upper()[0]