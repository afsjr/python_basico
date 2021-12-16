import re
import requests
lista = []
requisicao = requests.get('https://www.ghenos.net/es/contactos/')

padrao = re.findall(r'[\w-]+@[\w-]+\.[\w-]+', requisicao.text)

lista.append(padrao)

if padrao:
    print(padrao)
    for i in padrao:
        print(i)
else:
    print('padrao não encontrado')