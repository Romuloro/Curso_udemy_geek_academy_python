"""
Sorted

Obs.: Não confundir com o sort() que serve só pra listas. Já o sorted funciona
com qualquer iterável.


"""

num = (6, 1, 8.9, 10, 2, 4.5)

num1 = sorted(num)  # Retorna sempre um lista, com os valores ordenados
print(num1)

num2 = sorted(num, reverse=True)
print(num2)

"""
Reversed

OBS.: Não confundir com o reverse de list.
A função reverse só funciona com listas, porém a função reversed inverte
qualquer iterável.

A função reversed retorna um iterável chamado List reverse Iterator

"""

lista = [1, 2, 3, 5, 6]
resultado = reversed(lista)

for letra in reversed('A madrugada apenas começou'):
    print(letra, end='')


# Com o slice de strings
print('\n')
print('ta foda'[::-1])
