"""
Preservando metadatas

Metadados - São dados intrisecos em arquivos

Wraps - São funções que envolvem elementos com diversas finalidades

"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'VocÊ está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b

#print(soma(10,45))

#print(soma.__name__)
#print(soma.__doc__)

# Resolução do problema

from functools import wraps

def ver_log1(funcao):
    @wraps(funcao)
    def logar1(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'VocÊ está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar1


@ver_log1
def soma1(a, b):
    """Soma dois números."""
    return a + b

print(soma1(10,45))

print(soma1.__name__)
print(soma1.__doc__)
