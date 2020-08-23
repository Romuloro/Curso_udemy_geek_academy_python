"""
Dictionary Comprehension

# Sintaxe

{ chave: valor for valor in iterável}
"""

numero = {'a': 1, 'b': 2, 'c': 4}
quadrado = {chave: valor ** 2 for chave, valor in numero.items()}
print(quadrado)
