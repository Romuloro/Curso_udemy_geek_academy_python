'''
Documentando funções com Docstrings

Obs.: Podemos ter acesso a documentação de uma função usando
__doc__
'''

# Exemplo

def diz_oi():
    '''
    Uma função simples que retorna a string Oi
    para o usuário.
    '''
    return 'Oi!'


'''
Entendendo o *args

O *args é um parametro de entrada função, pode ser chamado
de qualquer nome desde que comece com *.

O parâmetro *args utilizando em uma função, coloca os valores extras informados como
entrada em uma tupla.  
'''

# Entendendo o args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(1, 45, 7, 10, 8))

# Outro exemplo, agora desempacotando com o *
numero = [1, 2, 3, 7, 9, 6, 5]

print(soma_todos_numeros(*numero))


'''
Entendendo **kwargs

O **kwargs é um parâmetro utiliza os parametros nomeados e transforma eles em um
dicionário.

'''


def cores_favoritas(**kwargs):
    """

    :param kwargs:
    :return:
    """
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores_favoritas(Romulo='Vermelho', Marcio='Azul', Elissa='Verde')

# A ordem dos parâmetros é: (parâmetro obrigatório, args, ñ obrigatório, kwargs)

# Desempacotando com o **kwargs usando o **

