'''
Você deve ler um conjunto de valores correspondentes a pagamentos (valores negativos) e recebimentos (valores positivos) e informar o balanço final.
'''

print('\nVocê deve ler um conjunto de valores correspondentes a pagamentos (valores negativos) e recebimentos (valores positivos) e informar o balanço final.\n')


balanço = []
repetição = 0
movimentação = int(input('Insira o número de movimentações a realizar: '))

while movimentação != repetição:
    balanço.append(float(input('\nInsira o valor movimentado: ')))
    repetição += 1

print('\n%.2f' % (sum(balanço)))