'''
Qual problema você tem que resolver?

Dada uma palavra, seu programa deve ler um conjunto de linhas e verificar quantas vezes aquela palavra se repete no texto
encerra com '.'

'''

print('\nDada uma palavra, o programa deve ler um conjunto de linhas e verificar quantas vezes aquela palavra se repete no texto. Encerre com "."\n')

procurar = input('\nInsira o que será buscado: ')

repet = []

while True:
    inserir = input('\nInsira o texto: ')
    repet.append(inserir.count(procurar))
    if inserir == '.':
        print(f'\nSua busca foi encontrada {sum(repet)} vezes')
        break