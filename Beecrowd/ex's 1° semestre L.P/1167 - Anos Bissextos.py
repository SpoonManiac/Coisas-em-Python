inicio = int(input())
anofim = int(input())

cont = 0

for ano in range(inicio, anofim + 1):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(ano)
        cont += 1
      
print(f'bissextos: {cont}')
