tamanho = int(input('Insira o tamanho de uma matriz quadrada: '))
lista = []

a='True'

for i in range(tamanho):
  lista.append([int(i) for i in input('\nInsira a linha da matriz em sequência: ').split()])
  if sum(lista[i])!=0:
    a='False'

print(a)