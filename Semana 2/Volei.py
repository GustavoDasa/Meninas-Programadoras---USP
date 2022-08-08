''''
Fábrica de placares eletrônicos
Todos sabem que você é fanática por vôlei e, por isso, criou sua própria empresa de placares eletrônicos. Para testar o programa que os juízes utilizam para inserir cada ponto do jogo, você tem que fazer um programa para processar a pontuação parcial de um set.
''''

# Seu programa recebe os pontos de um set, um por linha: o valor 1 indica ponto do time 1, e o valor dois indica ponto do time 2. 
# Seu programa deve aceitar pontos até que o set acabe, e imprimir o placar final do set.


rodada = 0
timeA = 0
timeB = 0

while (timeA < 25 and timeB < 25) or abs(timeA-timeB)<2:
    p = int(input())
    if p == 1:
        timeA += 1
        rodada +=1
    else:
        timeB +=1
        rodada +=1
print(timeA,'x',timeB)