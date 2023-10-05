temps = []
tempo = int(input())

def calculoM():
  media = sum(temps) / len(temps)
  return media

def exibeMedia(media):
  print(f'MEDIA: {media:.2f}')

def abaixoMedia(media):
  if(tempo < media):
    print(tempo)

def adicionaTempoLista():
  temps.append(tempo)

while (tempo >= 0):
  adicionaTempoLista()
  tempo = int(input())

exibeMedia(calculoM())

for tempo in temps:
  if ( tempo >= 0 ):
    abaixoMedia(calculoM()) 
