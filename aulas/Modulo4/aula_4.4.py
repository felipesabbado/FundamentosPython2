"""4.4 Section 4 – The os module - interacting with the operating system"""

'''
# 4.4.2 Getting information about the operating system

from platform import uname

print(uname())
'''

'''
# 4.4.3 Creating directories in Python
import os

# os.mkdir('Section-4') # cria um diretório com o nome indicado
print(os.listdir()) # cria uma lista com todos os elementos do diretório atual

# 4.4.4 Recursive directory creation

os.makedirs('Section-4/aula_4')
os.chdir('Section-4')
print(os.listdir())

# 4.4.5 Where am I now?

os.chdir('../') # muda o diretório
print(os.getcwd()) # informa o caminho absoluto atual

# 4.4.6 Deleting directories in Python

os.rmdir('aula_4') # Remove o diretório
# os.removedirs('Section-4/aula_4') # Remove diretórios recursivamente
'''
'''
# 4.4.7 The system() function
# Permite passar o comando direto para o sistema operacional
import os

value = os.system('mkdir my_dir')
print(value)
os.system('dir')
value = os.system('rmdir my_dir')
print(value)
'''
