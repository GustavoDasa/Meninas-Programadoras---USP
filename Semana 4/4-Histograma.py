lista = [int(i) for i in input('Insira uma sequência de valores: ').split()]

for i in range( len(lista) ):
  
    if lista[i] % 2  ==  0:
      
        print(lista[i] * '*')
    else:
        print(lista[i] * '.')