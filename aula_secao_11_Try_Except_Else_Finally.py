"""
Try / Except / Else / Finally

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código.
Assim que o programa pare de funcionar e o usuário receba mensagens de erro
inesperadas.

A forma mais simples é:
try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

Dica de quando e onde tratar o código:
Toda entrada do usuário deve ser tratada.

Finally é geralmente utilizado para fechar ou desalocar recursos.
"""


def elevado(num1, num2):
    try:
        return num1**num2
    except TypeError as err:
        print(f'Deve ser posta na variáveis de entrada um inteiro ou float {err}')


# Com erro
print(elevado(6, '8'))

# Sem erro
print(elevado(5, 3))

try:
    num = int(78)
except ValueError as err2:
    print(f'Deu erro de tipo {err2}')
else:
    print(f'O usuário digitou {num}')
finally:
    print(f'Estamos executando o finally')

# Obs.: O bloco finally é SEMPRE executado. Independente se houver exceção ou não.
