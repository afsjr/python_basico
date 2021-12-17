import datetime
import requests
import json


cidade = input('Qual cidade deseja saber o clima ? : ')
try:
    requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade+ '&appid=6ad3139525cc940cc7c4849517bbe066')
    dado_clima = json.loads(requisicao.text)

    print('')
    print('==========Tempo agora pelo Mundo ==============')
    print('Cidade: ', dado_clima['name'])
    print('Hora da pesquisa', datetime.datetime.now())
    print('Condição do tempo -> ', dado_clima['weather'][0]['main'])
    print('Temperatura em ', dado_clima['name'], 'é ', int(dado_clima['main']['temp']) - 273, 'ºC')
except Exception as erro:
    print('informação não disponível no momento \nTente mais tarde')


