"""
Generators - Tuple Comprehension

O ocupa menos espaço na memória que o list comprehension
"""

# Exemplo

nomes = ['Raquel', 'Romulo', 'Rafael', 'Fernando']
print(list((nome[0] == 'R' for nome in nomes)))

# Iterar no Generators

gen = (x ** 2 for x in range(1, 11))
print(gen)

for num in gen:
    print(num)
