divida = int(input())
pagamento = int(input())
contagem = 0

while divida > 0:
    contagem += 1

    if divida >= pagamento:
        antes = divida
        divida = divida - pagamento
        depois = divida
    else:
        antes = divida
        divida = divida - divida
        depois = divida

    print(f'pagamento: {contagem}')
    print(f'antes = {antes}')
    print(f'depois = {depois}')
    print('-----')


                OU

valor_divida = int(input())
valor_mensal = int(input())
pagamento = 0

while valor_divida > 0:
    pagamento += 1
    print (f'pagemnto: {pagemnto}')
    print (f'antes = {valor_divida}')
    if valor_mensal < valor_divida:
        valor_divida -=valor_mensal
    else:
        valor_divida = 0
    print (f'depois = {valor_divida}')
    print (5 * '-')
