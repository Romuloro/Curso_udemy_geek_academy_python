"""
Expressões Lambda

- Conhecidas por expressões lambdas, são funções sem nome ou seja funções anônimas.

# Função em python
def soma(a,b):
    return a+b

 - Geralmente são usadas para ordenações e filtragem de dados.
"""

# Sintaxe

expre = lambda x: (4 * x) + (5/x)
print(expre(3))
# A função lambda só funciona quando é anexada a uma variável. Porém não é a melhor forma.

# Forma correta

pessoas = ['Élissa dos Santos', 'Matheus Thuron', 'Rômulo Rodrigues de Oliveira',
           'Rodrigo Bijani']
print(pessoas)

pessoas.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(pessoas)


def equacao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


print(equacao_quadratica(2, 7, -2)(2))
