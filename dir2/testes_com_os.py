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

for elemento in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{elemento}.txt')

# Assertiva
assert len(os.listdir('.')) == 4

# Remover aequivo
os.remove('xpto.txt')

arq = os.listdir('.')
print(sorted(arq))