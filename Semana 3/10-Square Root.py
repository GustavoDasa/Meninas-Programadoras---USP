from math import sqrt

print('Neste programa, dados x e y iniciais e finais (separados por espaço), será retornado a norma do vetor.')

x1, y1 = [float(i) for i in input('\nInsira x y do início: ').split()]
x2, y2 = [float(i) for i in input('\nInsira x y do fim: ').split()]

dois_pontos = sqrt((x2-x1) ** 2 + (y2 - y1) **2)

print('\nFoi percorrido a distância de %.1f u.m.' % (dois_pontos))