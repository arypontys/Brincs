class Ordenar_lista:
    try:
        lista = open('ordenar_lista/lista.txt', 'a')
        
    except:
        print('Arquivo não encontrado! ')

    else:
        lista.writelines(['\nNova linha!', '\nNova lina 2', '\nNova linha 3'])
        lista.close()