import requests
import json
import time

while True:
    time.sleep(4)
    try:
        requis = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
    except:
        print('Não temos cotação disponível')

    padrao = json.loads(requis.text)

    print(' ============================ ')
    print('cotação atualizada em -> ', padrao['EURBRL']['create_date'])
    print(padrao['USDBRL']['name'],' = ', padrao['USDBRL']['high'])
    print(padrao['EURBRL']['name'],' = ', padrao['EURBRL']['high'])
    print(' ============================ ')
    print('')
