"""
Entendendo
Iterators: ele é um objeto da programação que por ser interado.
Um objeto que retorna um dado, sendo 1 elemento por vez, quando uma função next é chamada.

Iteraveis: um objeto que irá retornar um iterators, quando a função iter() for chamado.



"""

nome = 'Romulo'  #É um iteravel mas não um iterator.
numeros = [1,2,3,4,5]  #É um iteravel mas não um iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it2))



