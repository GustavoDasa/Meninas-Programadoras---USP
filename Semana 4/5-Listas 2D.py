tamanho = int(input('Insira o tamanho de uma matriz quadrada: '))
lista = []

for i in range(tamanho):
  lista.append([int(i) for i in input('\nInsira a linha da matriz em sequência: ').split()])

print()

for linha in range(tamanho):
  print(lista[linha])