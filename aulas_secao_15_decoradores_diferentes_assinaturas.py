# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

# Teste
print(saudacao('Élissa'))

# Refazendo

def gritar_m(funcao):
    def aumentar_m(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar_m

@gritar_m
def ordenar_m(principal, acompanhamento):
    return f'Olá, eu gosaria de {principal} acompanhado de {acompanhamento}, por favor!'

# Teste 2
print(ordenar_m('Strogonoff', 'Batata Palha'))
