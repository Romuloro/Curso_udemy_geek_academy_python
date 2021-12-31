"""
Propriedades -

getters - pega os valores
setters - modificam os valores dos mesmos.

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__titular

"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


conta1 = Conta('Romulo', 3000, 5000)
conta2 = Conta('Élissa', 2000, 5000)

print(conta1.extrato)
print(conta2.extrato)
print(conta1.saldo)
conta2.limite = 15000
print(conta2.limite)




