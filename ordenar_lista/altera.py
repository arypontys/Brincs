try:
    with open('ordenar_lista/lista.txt', 'r+', encoding='utf-8') as a:
        texto = a.readlines()

    with open('ordenar_lista/lista2.txt', 'w') as f:
        for linha in texto:
            f.write(linha.replace('[', '*'))
            
except:
    print('O arquivo não existe!!')

else:
    a.close()
    with open('ordenar_lista/lista.txt', 'w', encoding='utf-8') as b:
        b.write(f)