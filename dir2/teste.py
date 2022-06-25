# Arquivo de testes
from datetime import date
data = str(input('Entre com sua data de aniversário:  '))

data_aniversário = data.split('/')
dia = data_aniversário[0]
mes = data_aniversário[1]
ano = int(data_aniversário[2])
idade = ano - date.today().year

print('Você nasceu em {} de {} de {} e tem {} anos de idade. '
.format(dia, mes, ano, idade))