"""
Debugando com PDB

PDB - Python Debugger

"""

# Exemplo


def f_quadratica(a, b, c, x):
    try:
        return (a * x) ** 2 + (b * x) + c
    except (ValueError, TypeError) as err:
        return f'Ocorreu o erro {err}'


print(f_quadratica(4, -5, 2, 1.7))

# Para usar o Python Debugger, precisamos importar a biblioteca pdb utilizando
# a função set_trace()

# Comando básicos do Pdb:
# l (listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução)
