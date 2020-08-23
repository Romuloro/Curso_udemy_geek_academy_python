"""
Levantando os próprios erros com raise

raise - Lança exceções.

OBS.: Não é uma função. É uma palavra reservada, assim como def ou qualquer outra em python.
Usado para criar nossas próprias exceções e mensagens de erro.

Sintaxe
raise TipoDoErro ('Mensagem de erro')

"""


def color(texto, cor):
    if type(texto) is not str:
        raise TypeError("A variável texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A variável cor precisa ser uma string.")
    print(f'O texto {texto} sera impresso na cor {cor}.')


roxo = [1, 2]
color("Estou testando", "roxo")
