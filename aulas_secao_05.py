"""
Estruturas lógicas e Condicionais em Python

Not (não); And (e); Or (ou); Is (é)

Operadores unitários: not
Operadores binários: and e or e is
"""

# Condicionais - IF, ELSE, ELIF

idade = 18
#IF, ELSE, ELIF

if idade > 18:
    print("maior de Idade")
elif idade == 18:
    print("Serviço Militar")
else:
    print("menor de idade")

#AND, OR, NOT, IS

ativo = True
logado = False

if ativo == True and logado == False:
    print("Por favor efetue o login")
elif ativo and logado:
    print("Bem vindo ao sistema!")
else:
    print("Não existe usuário")

campeao = False
print(not campeao)
print(campeao is True)
