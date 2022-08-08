'''
Enchendo a carteira
Você ganhou uma carteira nova para guardar as suas notas de dinheiro. Dado o numero de notas e o valor de cada uma, quanto você colocou na carteira?
'''


notas = int(input())

carteira = []

while len(carteira) < notas:
    carteira.append(int(input()))

print(sum(carteira))