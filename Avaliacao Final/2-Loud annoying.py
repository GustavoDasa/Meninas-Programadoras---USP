while True:
    inserido = input('Digite um texto ou "." para terminar: ').upper()
    if inserido == '.':
        print('BYE')
        break
    else:
        print(inserido)