print('\nSeu programa deve consumir a sua própria condição de parada e, depois, consumir linhas da entrada até que seja fornecida a condição de parada lida originariamente, contando o número de linhas consumidas\n')

parar = input('\nInsira um texto para fechar: ')

z = 0

while True:
    x = input('Insira os textos')
    z += 1
    if x == parar:
        print(z-1)
        break