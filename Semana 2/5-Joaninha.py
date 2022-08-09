'''
Programa embarcado na Joaninha (aspirador automatizado)

- Quando a Joaninha é ligada, o programa captura da bateria um valor inteiro entre 0 e 100, correspondente à porcentagem de carga disponível.
- A Joaninha só funciona com carga mínima maior que 5%.
- Antes de cada movimento, o programa obtém informações de dois sensores. O primeiro sensor informa B de bateu ou L se a área livre à frente. O segundo sensor informa A se tem um Abismo, ou P se há Piso para avançar
- Para controlar a Joaninha, seu programa emite os comandos virar, em caso de necessidade, ou avançar, sempre que possível. Quando não há bateria disponível para trabalhar, seu programa avisa que é hora de recarregar.  Junto com cada comando, seu sempre programa informa o quanto de bateria resta na Joaninha.
- Cada movimento de avançar consome 1% de bateria. Cada movimento de virar consome  5% de bateria.
'''

bateria = int(input())

while True:
    comando = []
    if bateria <= 5:
        print('recarregar:', bateria)
        break
    comando.append(input().upper())
    comando.append(input().upper())
    if comando[0] =='B' or comando[1] =='A':
        bateria -= 5
        print('virar:', bateria)
    else:
        bat -= 1
        print('avançar:', bateria)