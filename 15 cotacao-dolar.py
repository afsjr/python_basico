import datetime

import requests
import json
import time

while True:
    time.sleep(1)
    try:
        requis = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
    except:
        print('Não temos cotação disponível')

    quotation = json.loads(requis.text)

    print(' ============================ ')
    print('cotação atualizada em -> ', datetime.datetime.now())
    print(quotation['USDBRL']['name'], ' = ', quotation['USDBRL']['high'])
    print(quotation['EURBRL']['name'], ' = ', quotation['EURBRL']['high'])
    print(' ============================ ')
    print('')
