numero = int(input())
letra = ord('A')
numerolinha = 1
while numerolinha <= numero:
    posiçãoletra = 1
    while posiçãoletra <= numerolinha:
        print(chr(letra), end='')
        posiçãoletra += 1
    letra += 1
    print()
    numerolinha += 1
