"""
Dicionários

Dicionários são coleções do tipo chave/valor.
Dicionários são representados por {}.
    - Chave e valor são separados por :.
    - Podendo ser qualquer tipo de dados.
"""

# Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'fr': 'França'}
print(type(paises))
print(paises)

# Forma 2
paises1 = dict(br='Brasil', eua='Estados unidos', fr='França')
print(paises1)

#Acessando elementos

# Forma 1 - Via []
print(paises['br'])
print(paises['fr'])

# Forma 2 - Vie get - Recomendado
print(paises.get('br'))
print(paises.get('eua'))

# Atribui o valor  None, quando a chave não for encontrada.
pais = paises.get('fr')
# Pode-se atribuir um valor padrão para quando a chave não for encontrada.
pais = paises.get('fr', 'Não encontrado')

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 400, 'mar': 30}

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) # Atualizar dados
print(receita)

# Remover

# Forma 1 - É retornavel
receita.pop('mar')
print(receita)

# Forma 2 - Não é retornavel
del receita['fev']
print(receita)


# Teste
teste1 = list(range(5, 16))
teste2 = list(range(9, 20))

print(teste1[2])

posicao = {'X': teste1, 'Y': teste2}
print(posicao)
x = posicao.get('X')
print('X é:', x)
print(x[1:6])



# Métodos de Dicionários

d = {'a': 1, 'b': 2, 'c': 5}

# Copiando um dicionário para outro
#   Forma Deep copy é igual a lista
#   Forma Shallow copy é igual a lista

# Criação de dicionário
#posicao = {}.fromkeys(['X', 'Y', 'Z'], 12.0)
#print(posicao)

receita1 = receita.get('mai')
print(receita1)
print(type(receita1))

# Interar sobre dicionários

posicao = {}


