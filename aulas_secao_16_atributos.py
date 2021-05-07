"""
Atributos  -

Em python, dividimos os tributos em 3 grupos:
    - De instância
    - De classe
    - Dinâmicos

Atributos de instância: São atribuitos declarados dentro do método construtor.
Obs.: Método construtor: È um método especial utilizado para a construção do objeto.

"""

# Atributo de instância: Significa, que ao criamos instância/objetos de uma classe, todas elas terão estes atributos.


class Lampada:

    def __init__(self, voltagem, cor):  # Método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


# Atributos públicos ou privados
#   Atributos  privados em python: usar __ no início do atributo.
#   Atributos publicos em python: Todos por padrão.

class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha


user = Acesso('pipipopo@gmail.com', '789456')
#print(user._Acesso__senha)  # Name Mangling: Temos acesso a atributos privados


# Atributos de Classe: São atributos que são declarados diretamente na classe,
# ou seja, fora do construtor. Geralmente já inicializamos um valor e este valor é
# compartilhado em todas as instâncias da classe.

p1 = Produto('Chocolate', 'Comida', 3.99)
p2 = Produto('Mouse', 'Wardware', 40.99)

# Refatorar a classe Produto:

class ProdutoCoreto:

    imposto = 1.05

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * ProdutoCoreto.imposto)


p1_c = ProdutoCoreto('Chocolate', 'Comida', 3.99)
p2_c = ProdutoCoreto('Mouse', 'Wardware', 40.99)

print(p1.valor)
print(p2.valor)
print(p1_c.valor)
print(p2_c.valor)


# Atributos Dinâmicos: É um atributo de instância que pode ser criado em tempo de execução.
# Obs.: Este atributo será exclusivo da instância que o criou.
# Deletando atributos:

