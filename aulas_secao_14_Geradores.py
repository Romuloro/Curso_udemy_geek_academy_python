"""
Geradores

- Geradores (Generators) são iteradores.
Obs.: O contrário não é válido.
     - Generators podem ser criados como funções geradoras
     - Funçoẽs geradores utilizam a palavra reservada yield
     - Generators pode ser criados como Exoressões Geradoras.

Diferenças entre Functions e Generator Functions:

Função
 - Utiliza return
 - Somente uma vez
 - Quando executada returna um valor


Generator Functions
 - Utiliza yield
 - Multiplas vezes
 - Quando executada returna um Generators

"""

# Exemplo de genetaors functions:

def cont_ate(max):
    contador = 1
    while contador <= max:
        yield contador
        contador = contador + 1

gen = cont_ate(5)

for num in gen:
    print(num)

