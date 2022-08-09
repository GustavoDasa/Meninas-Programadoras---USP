'''
Vamos soprar velinhas!

Depois de ler o número de velinhas, seu programa aguarda o aniversariante soprar com força suficiente para apagar cada uma delas para dar-lhe parabéns pelo aniversário
O aniversariante consegue apagar apenas uma vela de cada vez'
'''


anos = int(input()) #entrada do valor de anos completados

velasApagadas = 0

while velasApagadas < anos:
    x = len(input())
    if x > 6:
        print('bom sopro!')
        velasApagadas += 1
    elif x >= 4:
        print('um pouco mais de força no sopro!')
    else:
        print('precisa de muito mais força no sopro!')

print('Parabéns para pelo seu aniversário de',a,'anos!')