'''
LOOP FOR: estrutura de repetição, sendo o for uma dessas estruturas.
'''
nome = 'Romulo Rodrigues'
# Exemplo de for com string
for letra in nome:
    print(letra)

# Exemplo de for lista
lista = [1, 6, 8, 10, 89]

for numero in lista:
    print(numero)

# Exemplo de for em range

for numero in range(1, 10):
    print(numero)

# Exemplo for com enumerate

for valor in enumerate(nome):
    print(valor)

for _, valor in enumerate(nome): #Colocar o _, exclue o interador da interação
    print(valor)

##################################################################
n = int(input('Quantas vezes quer elevar o npumero 2?'))
for i in range(1, n+1):
    re = 2**i
    print(re)

##################### RANGE #############################################
# Ranges são utilizados para gerar sequências numéricas, de maneira específica

# Forma 1
for num in range(11):
    print(num)

# Forma 2
for num1 in range(10, 15):
    print(num1)

# Forma 3
for num2 in range(0, 20, 5):
    print(num2)

for num3 in range(10, 0, -1):
    print(num3)

##################### BREAK #############################################

for num in range(1,12):
    if num == 10:
        break
    else:
        print(num)

