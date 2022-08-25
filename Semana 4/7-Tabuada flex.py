t=int(input('\nInsira o valor que desejar: '))
i=int(input('\nInsira de onde iniciar a tabuada: '))
f=int(input('\nInsira de onde finalizar a tabuada: '))

print('\nTabuada do',t,'de',i,'até',f)

for i in range(i,f+1,1):
    print(t,'x',i,'=',t*i)