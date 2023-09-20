# Definir a nossa lista de carrinho de compras
carrinhoCompras = input().split() # 1 2 3 4 => ['1', '2', '3', '4']

# Verificação se o carrinho não for vazio, converter os itens string para inteiros
if (carrinhoCompras != []):

  # Conversão de string para inteiros
  for i in range(len(carrinhoCompras)):
    carrinhoCompras[i] = int(carrinhoCompras[i])
    # ['3', '5'] => [3, 5]
  
# Função para adicionar um item à lista
def adicionar(lista, item):
  lista.append(item)

# Função para remover um item da lista
def remover(lista, item):
  if (item in lista):
    lista.remove(item)
  else:
    print(f'código {item} não encontrado')

# Função para exibir os itens da lista de forma ordenada
def exibir(lista):
  lista.sort()
  
  for i in range(len(lista)):
    if (i < len(lista) - 1):
      print(lista[i], end=' ')
    else:
      print(lista[i])

# Receber os comandos digitados (comando valor) pelo usuário 
comando = input().split()
# ['exibir']
# ['adicionar', '1']

# Estrutura de repetição enquanto "encerrar" não for digitado
while comando[0] != 'encerrar':
  # Se digitar "adicionar", executar a função que adiciona e assim por diante
  if (comando[0] == 'adicionar'):
    adicionar(carrinhoCompras, int(comando[1]))
  elif (comando[0] == 'remover'):
    remover(carrinhoCompras, int(comando[1]))
  else:
    exibir(carrinhoCompras)

  comando = input().split()

exibir(carrinhoCompras)
