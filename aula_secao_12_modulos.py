"""
Modulo Random

Modulo - são nada mais do que outros arquivos Python.

Modulo Random - Possui várias funções para geração de números pseudo-aleatórios.

Forma de utilização 1
- import random
Importa todo o modulo de forma a deixar todas as suas funções na memória.

Forma 2
- from random import random
Importar somente as funções que serão utilizadas.

"""

import random

print(random.random())  # retorna um número entre 0 e 1.

# uniform - é uma função com o objetivo de retornar valores pseudo aleatórios
# entre os números escolhidos, sem acrescentar o valor final. intervalo (].

print(random.uniform(10, 60))

# randint() - Gera valores inteiros pseudoaleatórios entre os valores estabelecidos

print(random.randint(8, 32))

# choices - Retorna um valor aleatório entre um iterável

jogadas = ['Pedra', 'Papel', 'Tesoura']

print(random.choice(jogadas))

# shuflle() - Embaralha os dados.

cartas = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'A']
mao = []

for i in range(7):
    random.shuffle(cartas)
    pegada = cartas.pop()
    mao.append(pegada)

print(mao)
