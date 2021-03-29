"""
Sistema de arquivos manipulação


"""

import os

#descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt'))
print(os.path.exists('geek'))

#criando arquivos
#os.mknod('university_test.txt') não funciona no win AtributeError

#Criando diretório unicos
#os.mkdir('p1_teste')

#Criando diretórios estruturados
#os.makedirs('p1_teste/p1/p2')

#Renomear diretório, tem que estar vazio
#os.rename('arquivo original', 'nome a mudar')

#Renomear arquivos
#os.rename('.../.../arquivo.extensão', 'outro arquivo.extensão')

#Deletar arquivo: Eles não vão pra lixeiras, eles somem.
#os.remove('arquivo')

#Deletar diretórios: Só exclue diretorios vazios
#os.rmdir('diretório')

#Arquivos e diretórios tempoorários
import tempfile
#with tempfile.TemporaryDirectory() as top
#with tempfile.temporaryDirectory()
