velmaxima = int(input('Velocidade máxima permitida em (km/h): '))
velmotorista = int(input('Velocidade percorrida pelo motorista em (km/h): '))

multaleve = velmaxima + 10 
multamedia = velmaxima + 30

if velmotorista <= velmaxima:
    print('Velocidade normal')

elif velmaxima < velmotorista <= multaleve:
    print('Multa leve de R$ 85,13 e 3 pontos na carteira.')

elif multaleve < velmotorista <= multamedia:
    print('Multa média de R$ 127,69 e 5 pomtos na carteira.')

else:
    print('Multa gravíssima de R$ 574,62 e 7 pontos na carteira.')
