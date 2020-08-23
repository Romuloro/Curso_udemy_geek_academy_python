"""
Len, Abs, Sum and Round

len() - Retorna o tamanha, ou seja o número de itens de um iterável.

abs() - Retorna o valor absoluto de um número inteiro ou real.

sum() - Retorna a soma total dos elementos de um iterável.

round() - Retorna um número arredondado por n digitos de precisão após
a casa decimal.

"""

print(round(10.66666666, 3))
print(round(8.6))
print(round(1.5555555555555555567, 10))

"""
Zip

zip() - cria um iterável, chamado Zip object, agregando elemento
de cada um dos iteráveis passados cpm entrada em pares.
"""

# Exemplo
# Função importante para fazer o cruzamento no algoritmo genético??
lista12 = [1, 2, 3]
lista13 = [4, 5, 6]
zip1 = zip(lista12, lista13)
print(type(zip1))
print(list(zip1))

pai_1 = [2, 3, 6, 7, 4]
pai_2 = [3, 7, 9, 1, 8]
cruzamento = list(zip(pai_1, pai_2))
print(cruzamento)

# Revisitar este script para criar um modelo de cruzamento


