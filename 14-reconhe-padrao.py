import re
import requests

requisicao = requests.get('https://www.ghenos.net/es/contactos/')

padrao = re.findall(r'[\w-]+@[\w-]+\.[\w-]+', requisicao.text)

if padrao:
    for i in padrao:
        print(i)
else:
    print('padrao não encontrado')