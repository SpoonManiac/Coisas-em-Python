
def enigma(L):
    d = {'?': 0, '!':0} #oque significa essas chaves
    c = set()
    for x in L:
        if 'A' <= x <= 'Z':
            d['?'] += 1
        elif '0' <= x <= '9':
            d['!'] +=1
        else:
            c.add(x)
    return(d,c)

resultado = enigma('HHEllo123')
print(resultado[0])
c = resultado[1]
print(c)