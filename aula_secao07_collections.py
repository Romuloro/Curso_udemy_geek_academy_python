'''
Módulo Collections - Counter

Counter - Recebe um interavél como parâmetro e cra uma objeto do tipo Collections Counter
que é parecido co um dicionário, contendo como chave o elemento da lista passada como parâmetro
e como valor a quantidade de ocorrências desse elemento.

'''

# Importando o Counter
from collections import Counter

lista = [1, 2, 4, 4, 5, 8, 8, 9, 1, 1, 7]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

texto = "O texto informal é, portanto, bastante comum em conversas cotidianas" \
        "e mensagens de celular. Por outro lado, a linguagem formal" \
        "(registro formal) é aquela usada em situações que requerem seriedade" \
        "ou quando não há familiaridade entre os interlocutores"
print(texto)
palavras = texto.split()
result = Counter(palavras)
print(result)

'''
Módulo collection - Default Dict

Tudo que ocorre em um dicionário ocorre no Default Dict
Diferenças: Ao criar um dicionário criando o Default Dict, nós informamos um valor default
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um
valor definido. Caso tentemos acessar uma chave não existente, essa chave será criada
e o valor default será atribuido.
'''

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python Essencial'
print(dicionario)

print(dicionario['outro'])
print(dicionario)

'''
Módulo Collections - Ordered Dict

Em um dicionário, a ordem de inserção dos elementos não é garantida. Com
Ordered Dict a ordem é mantida.
'''
ex = {'a': 1, 'c': 5, 'z ': 46}

# Importando
from collections import OrderedDict

'''
Módulo Collections - Named Tuple
São Tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.

'''
# Importando
from collections import namedtuple

# Forma 1: Declaração
cachorro = namedtuple('cachorro', 'idade raça nome')
cachorro = namedtuple('cachorro', 'idade, raça, nome')
cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando
ze = cachorro(idade=0.8, raça='Vira-lata', nome='Zé')
gaya = cachorro(idade=7, raça='Vira-lata', nome='Gaya')
print(ze)
print(gaya)

# Acessar os dados
print(ze.raça)
print(ze.idade)
print(ze.nome)

'''
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
'''

# Importando
from collections import deque

deq = deque('geek')
print(deq)
deq.append('y') # Adiciona no final
