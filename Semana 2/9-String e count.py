'''
Contando ocorrências de uma substring em uma string
'''

print('\nContando ocorrências de uma substring em uma string\n')

encontrar = input('\nInsira o texto que quer encontrar: ') # texto que queremos encontrar

texto = input('\nInsira um texto: ') # texto onde iremos procurar

normal = texto.count(encontrar)  # busca de valores com correspondência exata

capit = texto.lower().count(encontrar.lower())   # busca de valores com correspondência geral

print(f'\nFoi encontrado {normal} exatos.')
print(f'Foi encontrado {capit} parecidos.')