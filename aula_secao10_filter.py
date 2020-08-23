"""
Filter

A função serve para filtrar dados de uma determinada coleção.
"""

import statistics as st

# Dados coletados
valores = (1.3, 2.6, 5.7, 6.7, 8.1, 9.5)

# Calculando a médias dos dados utilizando a função mean()
media = st.mean(valores)
print(media)

# filter recebe duas entradas (função, iterável)

res = filter(lambda x: x > media, valores)
print(list(res))

lugares = ['', 'Alagoas', 'Rio de Janeiro', 'Máceio', 'Fortaleza', '', 'Manaus']
print(lugares)
res1 = filter(None, lugares)
print(list(res1))

"""
A diferença entre o map e o filter é:
O map recebe um função uma iterável e retorna um objeto mapeando a função para cada elemento do iterável.
O filter recebe uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.
Retorna valores booleanos.
"""

# Combinar filter e map

nome = ['Vanessa', 'Ana', 'Maria']  # Só pode ser professora se tiver menos de 5 letras.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nome)))
print(list(lista))
