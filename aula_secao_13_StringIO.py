"""
StringIO > Utilizamos para ler e criar arquivos em memória

"""

from io import StringIO

mensagem = 'Só para teste'
arquivo = StringIO(mensagem)

print(arquivo.read())

