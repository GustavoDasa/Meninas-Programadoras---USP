# Verifica a atividade da pessoa, baseado nas entradas, sendo "m"=exerceu atividade, e "f" para finalizar

z = []

while True:
    x = input()
    z.append(x)
    if x == 'f':
        if z.count('m') > (0.5*len(z)):
            print('ativo')
        else:
            print('sedentário')
        break