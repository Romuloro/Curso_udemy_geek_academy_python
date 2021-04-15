"""
Decoretors:
- São Funções;
- Envolven outras funções e aprimoram o seu comportamento
- Também são exemplos de Higher Ordem Functions
- Tem sintaxe própria, usando "@"

"""


# Decorators como funções (Sintaxe ñ recomendada)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')

    return sendo


def saudacao():
    print('Seja bem vindo(a)!')


# Testando 1
#saudacao()

#teste = seja_educado(saudacao)
#teste()

print('********************************************')


# Decorators com Syntax Sugar

def seja_educado_mesmo(funcao):
    def sendo_definitivo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_definitivo


@seja_educado_mesmo
def apresentando():
    print('Sou o Rômulo!')

apresentando()

