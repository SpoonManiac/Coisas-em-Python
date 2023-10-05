lista = []
hifens = '-'*20
oi = ""
lista_noivo = []
lista_noiva = []
lista_ambos = []
c_noivo = ""
c_noiva = ""

lista_apenas_um = []
nova_lista = []
while oi!= 'ACABOU':
    teste = str(input())
    oi = teste
    if(oi=='ACABOU'):
        break
    lista.append(teste)

for i in range(len(lista)):
    if ';noivo' in lista[i]:
       c_noivo= lista[i].replace(';noivo', '')
       lista_noivo.append(c_noivo)
    elif ';noiva' in lista[i]:
        c_noiva = lista[i].replace(';noiva', '')
        lista_noiva.append(c_noiva)


for a in lista_noiva:
   
    
    
    nova_lista.append(a)


for b in lista_noivo:
    nova_lista.append(b)

for y in lista_noiva:
    if y in lista_noivo:
        lista_ambos.append(y)

for x in nova_lista:
    if x not in lista_ambos:
        lista_apenas_um.append(x)

for _ in lista_ambos:
    if _ in lista_noiva:
        lista_noiva.remove(_)

for _ in lista_ambos:
    if _ in lista_noivo:
        lista_noivo.remove(_)


lista_sr = list(set(nova_lista))
lista_ordenada= sorted(lista_sr)
print(f'{hifens}')
print('LISTA FINAL')
print(f'{hifens}')
for c in lista_ordenada:
    print(f'{c}')
print('')


lista_noiva_sr = list(set(lista_noiva))
lista_ordenada_noiva= sorted(lista_noiva_sr)
print(f'{hifens}')
print('APENAS NOIVA')
print(f'{hifens}')
for h in lista_ordenada_noiva:
    print(f'{h}')
print('')

lista_noivo_sr = list(set(lista_noivo))
lista_ordenada_noivo= sorted(lista_noivo_sr)

print(f'{hifens}')
print('APENAS NOIVO')
print(f'{hifens}')
for i in lista_ordenada_noivo:
    print(f'{i}')
print('')

lista_ordenada_ambos = sorted(lista_ambos)
print(f'{hifens}')
print('POR AMBOS')
print(f'{hifens}')
for j in lista_ordenada_ambos:
    print(f'{j}')
print('')


lista_apenas_um_sr = list(set(lista_apenas_um))
lista_ordenada_apenas_um= sorted(lista_apenas_um_sr)
print(f'{hifens}')
print('POR APENAS UM DELES')
print(f'{hifens}')
for k in lista_ordenada_apenas_um:
 print(f'{k}')