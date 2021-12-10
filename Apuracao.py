import Lista

def apuracao_votos():
  print("Apuração de votos Governadores")
  for apuracao in Lista.Governadores:
    print('Candidato: '+Lista.Governadores[apuracao]['Nome']+' ',Lista.Governadores[apuracao]['votos'])
  print("Apuração de votos Presidente")
  for apuracao in Lista.Presidentes:
    print('Candidato: '+ Lista.Presidentes[apuracao]['Nome']+' ',Lista.Presidentes[apuracao]['votos'])
  