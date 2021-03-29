"""
Arquivos e navegação

Diretório raiz
windows > C:\
POSIX > /

Path
\'nome da pasta'
.. move um diretório acima
. diretório local

Usamos o módulo os
"""

import os

#getcwd() pega o diretório de trabalho corrente, returna o caminho absoluto

#para mudar o diretório, podemos utilizar o chdir()

# para chegar se o diretório é absoluto ou relativo isabs()

#podemos identificar o nome do sistema operacional
#print(os.name)
#print(os.getcwd())

# Juntar os diretórios
#n_dic = os.path.join(os.getcwd(), 'geek')
#os.chdir(n_dic)
print(os.getcwd())

#listar os arquivos no diretório
#print(os.listdir('C:\\'))

#scandir pega mais detalhes
diret = (list(os.scandir('C:\\')))

print(diret[0].name) #nome do arquivo
print(diret[0].is_dir()) #É um diretório?
print(diret[0].is_file()) #É um arquivo?
print(diret[0].inode()) #identificador na árvore de diretórios
print(diret[0].is_symlink()) #É um link?
print(diret[0].path) #Caminho até o arquivo
print(diret[0].stat()) #Estatisticas

#precisamos fechar o scandir
diret.close()
