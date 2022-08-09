'''
Seu programa deve ler entradas do usuário continuamente e imprimir o total de linhas lidas. 

deve parar apenas quando quando receber o caractere ponto final '.'

ao final, deve imprimir o número de linhas lidas, incluindo a que sinaliza a parada do programa
'''


texto = []

while True:
    inserido = input()
    texto.append(inserido)
    if inserido == '.':
        print(len(texto))
        break