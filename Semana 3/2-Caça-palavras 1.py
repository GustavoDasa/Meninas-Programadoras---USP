'''
Vamos construir uma versão do famoso jogo de caça-palavras!

Aquele no qual existe uma matriz cheia de letras e a gente tem que procurar algumas palavras nela. As versões mais complexas permitem palavras escritas em várias direções e sentidos!

Para construirmos um jogo de caça-palavras, precisamos saber quais palavras queremos caçar e em que matriz de letras vamos busca-las.

Vamos começar com uma versão assim:

- dada uma palavra a caçar

- e uma linha com um conjunto de palavras

- vamos verificar se a palavra a caçar está no conjunto de palavras
'''

palavra = input('Insira a palavra que deseja encontar: ')

texto = input('\nInsira um conjunto de palavras separadas por espaço: ')

lista = texto.split(' ')   # Separa o texto por espaço

if palavra in texto:
    print("")
    print(palavra,lista.index(palavra))
else:
    print('\nfalta',palavra)