'''
Contando ocorrências de uma substring em uma string
'''

encontrar = input() # texto que queremos encontrar

texto = input() # texto onde iremos procurar

normal = texto.count(encontrar)  # busca de valores com correspondência exata

capit = texto.lower().count(encontrar.lower())   # busca de valores com correspondência geral

print(normal)
print(capit)