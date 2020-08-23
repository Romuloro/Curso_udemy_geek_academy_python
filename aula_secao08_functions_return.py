'''
Funções com Parâmetros padrão
- Funções onde a passagem de parâmetros é opcional

# Exemplo
print()
'''


def exponencial(num, potencia=2):  # Torna a potência opcional
    return num ** potencia


print(exponencial(2, 3))
print(exponencial(4))

# Obs.: O valor default tem que ser no final da declaração

# Escopo - Evitar problemas e confusões.
# Variaveis locais se sobrepõem a variavel global.
# Variavel local só é reconhecida dentro de seu bloco.
