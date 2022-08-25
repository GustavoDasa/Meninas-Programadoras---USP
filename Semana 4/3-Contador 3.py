limite = int(input('Insira o valor para somar todos os múltiplos de 3: '))+3

lista = [ i*3 for i in range(limite//3) ]

print(sum(lista))