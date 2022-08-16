'''
Introdução

Para relaxar no intervalo da aula, algumas meninas inventaram um jogo de cartas assim: quatro meninas jogam em duplas, duas contra duas, e cada menina recebe uma carta com valores de 2 a 10. Ganha o jogo a dupla que possuir a maior carta.

No início do jogo, uma monitora dá uma carta (com a face para baixo!) para cada uma das quatro meninas. 

A seguir, a monitora pede para as quatro meninas apresentarem suas cartas. 

 Como o número de duplas é grande, a monitora  pediu para você fazer um programa que identifique qual dupla ganhou o jogo, ou se houve empate.

Entrada

Quatro linhas informando os valores das cartas na seguinte ordem:

carta da 1a menina da 1a dupla carta da 1a menina da 2a dupla carta da 2a menina da 1a dupla carta da 2a menina da 2a dupla

Saída

Valor da carta vencedora. Em caso de empate, imprima empate
'''


timeA = []
timeB = []

timeA.append(int(input('Carta da 1a menina da 1a dupla: ')))
timeB.append(int(input('\nCarta da 1a menina da 2a dupla: ')))
timeA.append(int(input('\nCarta da 2a menina da 1a dupla: ')))
timeB.append(int(input('\nCarta da 2a menina da 2a dupla: ')))

if max(timeA) == max(timeB):
    print('empate')
else:
    print()
    print(max(timeA+timeB))