totaldonation = 0
VicCoins = float(input())

while VicCoins != -1:
    totaldonation += VicCoins
    VicCoins = float(input())

convertion = totaldonation * 2.5

print(f'VC$ {totaldonation:.2f}')
print(f'R$ {convertion:.2f}')