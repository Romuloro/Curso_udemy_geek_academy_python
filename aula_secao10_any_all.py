"""
Any e All

all() -> Retorno True se todos os elementos do iterável for verdadeiros ou vazia.

any() -> Retorna True se algum dos elementos dos dados for verdadeiro e se tiver vazio é False.

"""

# Exemplo de all()
print(all([0, 1, 2, 3, 4])) # Como o zero é False vai dar False.

nomes = ['Carlos', 'Camila', 'Cassandra', 'Caio']
print(all([nome[0] == 'C' for nome in nomes]))

print(all([num for num in [1, 46, 7, 8, 19, 12] if num % 2 == 0]))

# Exemplo de any()
print(any([num for num in [1, 2, 3, 40, 0.6] if num > 10]))
print(any([num for num in [1, 2, 3, 4, 0.6] if num > 10]))
