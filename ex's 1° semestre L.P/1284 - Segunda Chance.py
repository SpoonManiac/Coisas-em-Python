qntAlunos = int(input())

def qntNotas():
    notas = []

    for u in range (qntAlunos):
        notas.append(float(input()))
    return notas

def obterNotasFinais (notasOriginais, novasNotas):
    qntNotasAlteradas = 0

    for i in range (len(notasOriginais)):
        if (novasNotas[i] == 10 and notasOriginais[i] < 10):
            novasNotas[i] = min(notasOriginais[i] + 2, 10)
            qntNotasAlteradas += 1
        else:
                novasNotas[i] = notasOriginais[i]
                
    return qntNotasAlteradas


def exibirNotasAlteradas(notasOriginais, notasFinais, qntNotasAlteradas):
    print(f'NOTAS ALTERADAS: {qntNotasAlteradas}')
    for i in range (qntAlunos):
        notaAlterada = ('*' if notasOriginais[i] != notasFinais[i] else '-')
        print (f'{notaAlterada}({i+1:03}) original: {notasOriginais[i]:05.2f} | final: {notasFinais[i]:05.2f}')


if (1 <= qntAlunos <= 999):
    notasOriginais = qntNotas()
    novasNotas = qntNotas()
    qntNotasAlteradas = obterNotasFinais(notasOriginais, novasNotas)
    exibirNotasAlteradas (notasOriginais, novasNotas, qntNotasAlteradas)
