'''
Uma professora do ensino fundamental está ensinando as crianças de sua sala a soletrar. As crianças gostaram tanto que pedem palavras o tempo todo, mas a professora não dá conta de verificar todas. Ela ficou sabendo que você está fazendo o curso de Meninas Programadoras e pediu para você ajudar de modo que as crianças possam usar um computador para informar cada uma das letras que formam uma palavra.

Nesta versão, seu programa primeiro lê a palavra que as crianças devem soletrar. A seguir, a criança digita uma sequencia de letras, uma por linha, e, quando terminar, digita o ponto final. Você sinaliza para a professora com True e False, respectivamente, caso a criança acerte ou não a palavra.

Nota:  depois do curso Meninas Programadoras, você querer aprender a como ler as palavras de um arquivo e, ainda, falar a palavra usando o áudio do computador, certo?
'''

lista = []
texto = list(input('Digite uma palavra para soletrar: ')) # transformando em uma lista de caracteres

while True:
    x = input('\nSoletre: ')
    if  x == '.':
        break
    lista.append(x)

if texto == lista:
    print('Você acertou!')
else:
    print('Você errou.')