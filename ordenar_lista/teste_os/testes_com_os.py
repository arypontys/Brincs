from genericpath import exists
from pathlib import Path
import os
import os.path
import shutil


# Caso o diretório não exista ele vai ser criado.
if not exists('dir2'):
    os.mkdir('dir2')

#ir para o diretório dir2
os.chdir('dir2')

# Criar arquivo xpto.txt
Path('xpto.txt').touch()


for cont in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{cont}.txt')

# Realizar a assertiva
assert len(os.listdir('.')) == 4


arq = os.listdir('.')
print(arq)
