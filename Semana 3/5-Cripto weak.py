'''
Criptografia

Criptografia é uma área da criptologia que estuda e prática princípios e técnicas para comunicação segura na presença de terceiros, chamados "adversários". Geralmente, a criptografia refere-se à construção e análise de protocolos que impedem terceiros, ou o público, de lerem mensagens privadas. (fonte Wikipédia)

Seu problema

Dada uma mensagem , você precisa trocar todas as ocorrências de um caractere específico por outro. 

Entrada

Três linhas. 

Na primeira, o caractere a ser trocado. Na segunda linha, o caractere que irá substituir o caractere a ser trocado. Na terceira linha, a mensagem a ser criptografada.

Saída

A mensagem criptografada.
'''

x = input('Insira o caracter para criptografar: ')
y = input('\nInsira o que sera colocado no lugar')

texto = list(input('Insira um texto para criptografar: ').lower())

for i in texto:
    if i == x:
        texto[texto.index(i)] = y


print(''.join(texto))