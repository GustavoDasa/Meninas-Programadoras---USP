'''
Caçando várias palavras em uma linha

Vamos continuar a caçar palavras? 

Desta vez

Seu programa recebe uma linha com uma ou mais palavras (na qual a caça ocorre) Seguido de outra linha com uma ou mais palavras a serem caçadas, obrigatoriamente presentes entre as fornecidas na primeira linha Seu programa produz uma linha para cada palavra caçada, com a posição onde ela foi encontrada
'''




texto = input('Insira um texto: ')

palavra = input('\nInsira palavras que estão na lista separadas por espaço: ')

lista = palavra.split(' ')   # Separa o texto por espaço

for i in lista:
  print()
  print(i,texto.index(i))