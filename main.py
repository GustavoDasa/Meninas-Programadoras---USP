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
    11: '11-Volei'}

darq3 = {
    1:'1-Balanco',
    2:'2-Caça-palavras 1',
    3:'3-Caça-palavras 2',
    4:'4-Cripto MP T3',
    5:'5-Cripto weak',
    6:'6-Duas contra duas',
    7:'7-Micos Game',
    8:'8-Soletrando até acertar',  
    9:'9-SOS Morse', 
    10:'10-Square Root',
    11:'11-Uma letra de cada vez'}

darq4 = {
    1: '1-Contador',
    2: '2-Contador 2',
    3: '3-Contador 3',
    4: '4-Histograma',
    5: '5-Listas 2D',
    6: '6-Ordem na bagunça',
    7: '7-Tabuada flex',
    8: '8-Zeros 2D'}

darq5 = {
    1: '1-Infinito enquanto dure',
    2: '2-Loud annoying',
    3: '3-Participação monitoria',
    4: '4-Passagem kids'
}

dsem = {2: 'Semana 2' , 3: 'Semana 3', 4: 'Semana 4', 5:'Avaliacao Final'}
dsarq = {2: darq2, 3: darq3, 4: darq4, 5: darq5}

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
        exec(open(f'{dsem[semana]}/{x[arq]}.py').read())
    except:
        print('\nTente Novamente!\n')
        continue
    finally:
        print("\nVolte do início...\n")

# Executa o programa		
if __name__ == "__main__":
	main()
