inicio = int(input())
fim = int(input())
quantprimos = 0

def primo(num):
    if num < 2:
        return False # AQUI NÃO É PRIMO
    elif num == 2:
        print (num)
        return True #ESSE É PRIMO
    else:
        for i in range (2,num):
            if num % i == 0:
                return False
        print (num)
        return True

# A LÓGICA
if (inicio <= fim <= 5000):
    for i in range (inicio, fim + 1):
        if primo (i):
            quantprimos += 1

    print (f'primos: {quantprimos}')
