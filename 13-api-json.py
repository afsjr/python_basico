import requests
import json
req = None

try:
    req = requests.get('http://www.omdbapi.com/?apikey=25ddb129&s=interstellar')
except:
    print('Erro na conexão')
    exit()


dicionario = json.loads(req.text)

print(dicionario)