p = 'tem monitorias OK! :-)'
r = 'não tem monitorias suficientes :-('

tamanho = int(input('Insira a quantidade de alunas: '))
nomes = []
result = {}


for i in range(tamanho):
    nomes.append(input(f'\nInsira o nome da Aluna {i+1}: '))
    result[i] = p
    for x in range(4):
        if int(input(f'\nInsira os minutos cumpridos da semana {x+1}: ')) < 120:
            result[i] = r

for i in range(tamanho):
    print()
    print(nomes[i],result[i])