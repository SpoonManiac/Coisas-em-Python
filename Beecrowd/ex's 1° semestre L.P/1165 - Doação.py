totaldoado = 0

valordoado = float(input())
while valordoado != -1.0:
    totaldoado += valordoado
    valordoado = float(input())
    
converte = totaldoado * 2.50

print (f'VC$ {totaldoado:.2f}')
print (f'R$ {converte:.2f}')
