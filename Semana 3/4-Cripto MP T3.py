texto = list(input('Insira um texto para criptografar: ').lower())

for i in texto:
    if i == 'a':
        texto[texto.index(i)] = '@'
    if i == 'o':
        texto[texto.index(i)] = '*'

print(''.join(texto))