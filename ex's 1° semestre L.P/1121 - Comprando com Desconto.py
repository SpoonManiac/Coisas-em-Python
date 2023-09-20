preçom = float(input())
qntm = int(input())

preçosdes = preçom * qntm
piriripinpin = (0.1 + 0.01*qntm) * preçosdes
preçocdes = preçosdes - piriripinpin 

print(f'{preçosdes:.2f}')
print(f'{preçocdes:.2f}')
