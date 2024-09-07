def eh_primo(numero):
    resultado = 1
    if numero < 2:
        resultado = None
        return resultado
        # return False
    for i in range(2, int(numero ** 0.5) + 1):
        print(i)
        if numero % i == 0:
            resultado = None
            return resultado
            # return False
    return resultado
    # return True

# Exemplo de uso
numero = 4
if eh_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
