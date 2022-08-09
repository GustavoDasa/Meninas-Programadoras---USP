'''
Vamos soprar velinhas!

Depois de ler o número de velinhas, seu programa aguarda o aniversariante soprar com força suficiente para apagar cada uma delas para dar-lhe parabéns pelo aniversário
O aniversariante consegue apagar apenas uma vela de cada vez'
'''


anos = int(input("Insira as velas que irá apagar: ")) #entrada do valor de anos completados

velasApagadas = 0

while velasApagadas < anos:
    x = len(input('\nAssopre forte! "fuh" : '))
    if x > 6:
        print('\nbom sopro!')
        velasApagadas += 1
    elif x >= 4:
        print('\num pouco mais de força no sopro!')
    else:
        print('\nprecisa de muito mais força no sopro!')

print('\nParabéns para pelo seu aniversário de',anos,'anos!\n')