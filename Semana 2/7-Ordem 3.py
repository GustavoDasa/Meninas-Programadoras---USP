print('\nSeu programa deve ler entradas do usuário continuamente e imprimir o total de linhas lidas.') 

print('\nDeve parar apenas quando quando receber o caractere ponto final "."')


texto = []

while True:
    inserido = input('\nInsira um texto: ')
    texto.append(inserido)
    if inserido == '.':
        print(f'\nSeu texto possui {len(texto)} parágrafos.')
        break