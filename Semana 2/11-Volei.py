'''
Fábrica de placares eletrônicos
Todos sabem que você é fanática por vôlei e, por isso, criou sua própria empresa de placares eletrônicos. Para testar o programa que os juízes utilizam para inserir cada ponto do jogo, você tem que fazer um programa para processar a pontuação parcial de um set.
'''

print('Insira os pontos de um set de vôlei, um por linha: o valor 1 indica ponto do time 1, e o valor dois indica ponto do time 2 até que o set acabe.')

rodada = 0
timeA = 0
timeB = 0

while (timeA < 25 and timeB < 25) or abs(timeA-timeB)<2:
    p = int(input(f'\nRodada {rodada+1}: '))
    if p == 1:
        timeA += 1
    else:
        timeB +=1
      
    rodada +=1
print(f'\nTime A {timeA} x {timeB} Time B')