'''
Problema

A professora do Ensino Fundamental gostou tanto do programa que você fez para o problema Soletrando que pediu para você fazer uma nova versão!

Ela quer que, em caso de erro em uma tentativa de soletrar a palavra, as crianças possam realizar novas tentativa elas mesmas! Para isso, vocês combinaram com as crianças que elas podem tentar quantas vezes quiserem, e que:

- quando elas acertarem, o programa imprime 8-) e termina

- quando elas errarem, o programa imprime 8-| e elas podem tentar a mesma palavra outra vez

Entrada

- Primeira linha: uma palavra simples  (sem espaços)

- Linhas seguintes: uma letra por linha, terminadas com ponto.

- Se as letras corresponderem corretamente à palavra da primeira linha, seu programa imprime 8-) e termina

- Caso contrário,  seu programa imprime 8-| e lê um novo conjunto de linhas terminado por ponto.

Saída

- uma sequencia de zero ou mais linhas com 8-|

- ultima linha: 8-)
'''



texto = list(input('Digite uma palavra para soletrar: ')) # transformando em uma lista de caracteres

while True:
    lista = []
    while True:
        x = input('\nSoletre: ')
        if  x == '.':
            break
        lista.append(x)

    if texto == lista:
        print('8-)')
        break
    else:
        print('8-|')