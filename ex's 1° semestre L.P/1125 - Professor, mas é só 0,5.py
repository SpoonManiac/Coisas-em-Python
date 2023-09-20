trabalho = float(input())
prova = float (input())
substituta = 10

media = (trabalho + prova) / 2
if media >= 6:
    print ('aprovado')
else:
    if prova < substituta and (trabalho + substituta)/2 >=6:
        print ('talvez com a sub')
    else:
        print('reprovado')
