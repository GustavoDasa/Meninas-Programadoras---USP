darq2 = {
    1: '1-Bolo de Aniversário',
    2: '2-Carteira - if while',
    3: '3-Dispositivos inteligentes',
    4: '4-Infinito enquanto dure',
    5: '5-Joaninha',
    6: '6-Ordem 2',
    7: '7-Ordem 3',
    8: '8-Ordem 4',
    9: '9-String e count',
    10: '10-Tentativa e erro',
    11: '11-Volei'
}
darq3 = {}
darq4 = {}

dsem = {2: 'Semana 2', 3: 'Semana 3', 4: 'Semana 4'}
dsarq = {2: darq2, 3: darq3, 4: darq4}


semana = 0
arq = 0
print(
    'Para selecionar um arquivo para rodar, navegue no diretório inserindo o valor correpondente.\n\nPara maior compreensão, visualize o arquivo no diretório antes de executá-lo.\n'
)


def Navegar():
    global x, arq, semana
    for i in dsem:
        print(i, '-', dsem[i])

    semana = int(input('\nInsira o valor da "Semana" correpondente: '))
    x = dsarq[semana]
    print('')
    for i in x:
        print(x[i])

    arq = int(input('\nInsira o valor do "Arquivo" correpondente: '))
    print('')

while True:
    try:
        Navegar()
        exec(open(f'Semana {semana}/{x[arq]}.py').read())
    except:
        print('\nTente Novamente!\n')
        continue
    finally:
        print("\nVolte do início...\n")

