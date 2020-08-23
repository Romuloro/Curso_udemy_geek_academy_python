'''
Conjuntos - estamos fazendo referencia a teoria dos conjuntos da matemática.

No python os conjuntos são chamados de sets.
- Da mesma formas que na matemáticas, sets, conjuntos não possuem valores duplicados;
- Não possuem valores ordenados;
- Elementos não são acessados via índices, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos e não nos
preocupamos com a ordenação, chaves, valores e itens duplicados.

Os sets são referenciados com chaves {}

Diferença entre conjuntos sets e dicionários
- Um dicionário tem chave/valor;
- Um set tem apenas valor;

'''

# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 1, 2, 3, 7})
print(s)
print(type(s))

# Forma 2 - Mais comum
s1 = {1, 2, 3, 3, 2, 4, 6, 7, 8, 8}
print(s1)
print(type(s1))

# Importante lembrar que não temos valores duplicados também não temos ordens
# Podemos iterar em um set normalmente
# Adicionando elementos em um set
s.add(40)
print(s)

# Remover elementos
# Forma 1
s.remove(1)
print(s)

# Forma 2
s.discard(3)
print(s)

# remover todos os pontos do conjunto usando o clear()
# fazer a união de conjutos usando o .union() ou usando o caracter pipe |
# Gerar a interseção utilizando .intersection() ou utilizando o caracter &
# A diferença entre conjuntos usando .difference()
