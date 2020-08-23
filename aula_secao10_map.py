"""
Map

- Com map, fazemos o mapeamento de valores para a função.

"""

import numpy as np

area = lambda r: np.pi * (r ** 2)

def c_area(r):
    return np.pi * (r ** 2)


print(area(2))
print(area(5))

raios = list(range(1, 21))
print(raios)

# Forma utilizando map recebe(função, interavel)

areas = map(c_area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 map com lambda
print(list(map(lambda r: np.pi * (r ** 2), raios)))

# Obs.: Após a primeira utilização (loop, conversão) ele zera.

