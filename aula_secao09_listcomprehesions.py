"""
List Comprehesion

- Utilizando List Comprehesion nós podemos gerar listas com dados processados a
partir de outro iterável.

* Sintaxe do List Compreshion
[ dado for dado in iterável]

"""
num = [1, 2, 3, 4, 5]

res = [num * 10 for num in num]
print(res)

"""
Para entender melhor oq ta acontecendo devemos dividir em duas partes:
    1) for num in num
    2) num * 10
"""

def quadrado(valor):
    return valor * valor


res1 = [quadrado(num) for num in num]
print(res1)

"""
Podemos adicionar estruturas lógicas ás nossas list comprehesion
"""

pares = [num for num in num if num % 2 == 0]
print(pares)
impares = [num for num in num if num % 2 != 0]
print(impares)
