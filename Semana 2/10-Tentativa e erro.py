'''
Que problema você tem que resolver?

Para passar o tempo, você programou um jogo no qual você "escolhe" um valor e depois deixa uma colega chutar valores até acertar o valor que você "escolheu". As regras são

primeiro você digita o número-alvo a ser encontrado depois você deixa sua amiga chutar um valor até que ela acerte

Portanto, depois do número-alvo escolhido inicialmente, seu programa deve iniciar um bloco de repetição que só termina quanto o valor que sua amiga chutou for igual ao que você escolheu inicialmente.

Ou seja, para cada chute
'''

valor = int(input('Insira um número para seu amigo adivinhar: '))
print('\n\n\n\n\n\n\n')


while True:
    chute = int(input('\nTente acertar o número: '))
    if chute == valor:
        print('\nAcertou!!!')
        break
    elif chute < valor:
        print('\nÉ maior!')
    else:
        print('\nÉ menor')