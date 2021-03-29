"""
Dunder main and Dunder name

Dunder name = __name__

Dunder main = __main__

Em python, são utilizados Dunders para criar funções, atributos e propriedades para não criar conflitos com os nomes
de variáveis de programação.
"""

vetor_test = [5,5,5,5,5,5,2,2,2,3,7,7,7,7,7]
vv = vetor_test[0:15:5]
print(len(vetor_test))
print(vv)

for i in range(len(vetor_test)):
    if (i % 5 == 0) and (vetor_test[i] == vetor_test[i-5]):
        print('aumenta mut para 0,2')
    else:
        print("mantem em 0,05")
