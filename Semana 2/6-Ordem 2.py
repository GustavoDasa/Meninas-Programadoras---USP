print('\nEnquanto não chegar um ponto final o programa deve ler entradas do usuário continuamente\n')

while True:
    entrada = input('\nInsira um texto: ')
    if entrada == '.':
        print('\nOk\n')
        break