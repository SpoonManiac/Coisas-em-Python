entrada = input().split()
a, b, c = entrada

maior = (int(a) + int(b) +abs(int(a)-int(b)))/2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c))) /2

print(f'{resultado} eh o maior')