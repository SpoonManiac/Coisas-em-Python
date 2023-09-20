entrada = input().split()
entrada2 = input().split()

cod, number, value = entrada
cod2, number2, value2 = entrada2

total = (int(number)* float(value) + (int(number2)) * float(value2))

print(f'VALOR A PAGAR: R$ {total:.2f}')