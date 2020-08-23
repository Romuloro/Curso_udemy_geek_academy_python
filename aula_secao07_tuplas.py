'''
Tuplas (tuple)

As diferenças das tuplas para as listas.

1) As tuplas são representadas por ()

2) As tuplas são imutaveis. Todas as operações em uma tupla gera uma nova tupla


'''

# CUIDADO 1:

tupla1 = (1, 2, 3, 4)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4
print(tupla2)
print(type(tupla2))

# CUIDADO 2:
tupla3 = (4) # não é tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # é tupla
print(tupla4)
print(type(tupla4))

# Tuplas são definidas pela vírgula e não pelo ()

# Criando uma tupla com range

rangetupla = tuple(range(5))
print(rangetupla)
print(type(rangetupla))

nometupla = ('Rômulo', 'Rodrigues', 'de', 'Oliveira')
nome, sobrenome1, de, sobrenome2 = nometupla
print(nome)
print(sobrenome1)
print(de)
print(sobrenome2)

# Métodos de adicão e remoção não existem em uma tupla
# Soma, Valor max, Valor min
tupla = (1.5, 2.0, 5.5, 8.7, 9.1)
print(tupla)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Interando sobre uma tupla

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos na tupla
tupla = (1.5, 2.0, 5.5, 8.7, 9.1, 1.5, 2.0)
print(tupla.count(2.0))

# TUPLAS SÃO UTILIZADAS QUANDO NÃO QUEREMOS QUE O CONTEÚDO DA COLEÇÃO SEJA ALTERADO

# Acesso a elementos de uma tupla
print(tupla[3:5])

# Por que utilizar tuplas?
# Tuplas são mais rápidas do que listas.
# Tuplas deixam seu código mais seguras, pelos conteúdos imutaveis.
