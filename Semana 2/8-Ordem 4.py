'''
Qual problema você tem que resolver?

Dada uma palavra, seu programa deve ler um conjunto de linhas e verificar quantas vezes aquela palavra se repete no texto
encerra com '.'

'''


procurar = input()

repet = []

while True:
    inserir = input()
    repet.append(inserir.count(procurar))
    if inserir == '.':
        print(sum(repet))
        break