'''
Listas funcionam como vetores/matrizes em outras linguagens, com a diferença
de serem DINÂMICO e também de podemos colocar QUALUQER tipo de dado.

As listas em python são representadas por [].
'''

lista1 = [1, 8, 71, 23, 64, 89, 4, 6]
som = lista1[2] + lista1[5]
print(som)
print(type(lista1))

lista2 = [[1, 2, 3], [4, 5, 6]]
lista3 = [[1, 2, 3], [4, 5, 6]]
print(lista2)
print(lista2[0])
soma = lista2[0] + lista3[0]
print(soma)

# O uso de SORT, ordenar lista
lista1.sort()
print(lista1)

# O uso de count, contabilizar o número de ocorrências de um valor em uma lista
print(lista1.count(23))

# Adicionar elementos em uma lista, utiliza-se a função append. Somente um elemento por vez
lista1.append(89)
print(lista1)
lista1.append([56, 27, 96])
print(lista1)
lista1.extend([789, 63, 71]) #Coloca cada valor na lista.
print(lista1)

# Inserir um novo elemento na lista informando a posição do índice, INSERT
lista1.insert(5, 100)
print(lista1)

# Inverter os valores e itens da lista, REVERSE
lista1.reverse()
print(lista1)

# Copiar uma lista
lista4 = lista1.copy()
print(lista4)

# Remover o último item de uma lista, ou qual vc escolher POP
print(lista1)
lista1.pop()
lista1.pop(9)
print(lista1)

# Converter string em lista, usando o SPLIT, o separador é algo que você escolher, ou o espaço.

# JOIN transforma lista em string.

# Interando com listas
lista5 = ['R', 'ô', 'm', 'u', 'l', 'o', ' ', 'R', 'o', 'd', 'r', 'i', 'g', 'u', 'e', 's']

for elemento in lista5:
    print(elemento)

####################################################3
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto, ou digite 'sair' para sair.")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

lista = []
lista.extend([33, 33, 33, 66, 66, 78, 78])
print(lista)

os300 = list(range(1, 301))
print(os300)

print(lista.index(66))

# Procurar o maior valor, o menor valor e o tamanho da lista?
print(sum(lista))
print(len(lista))
print(max(lista))
print(min(lista))

# Copiando uma lista para outra (Shallow copy e Deep copy)

# Deep copy (Nada que ocorre na lista criada interfere na lista anterior)
novalista = lista.copy()
novalista.append(45)
print(lista)
print(novalista)

# Shallow copy (Tudo que for adicionado na lista será adicionado a lista anterior)
novalista1 = lista
novalista1.append(45)
print(lista)
print(novalista1)
