print('Enchendo a carteira\nVocê ganhou uma carteira nova para guardar as suas notas de dinheiro. Dado o numero de notas e o valor de cada uma, quanto você colocou na carteira?\n')


notas = int(input('\nInsira quantas notas recebeu: '))

carteira = []

while len(carteira) < notas:
    carteira.append(int(input('\nInsira o valor das notas que recebeu, uma por ver: ')))

print('Você recebeu',sum(carteira),'em notas!')