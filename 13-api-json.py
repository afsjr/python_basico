import requests
import json
req = None

try:
    req = requests.get('http://www.omdbapi.com/?apikey=25ddb129&s=star+wars&type=movie')
except:
    print('Erro na conexão')
    exit()


dicionario = json.loads(req.text)

print(dicionario['Search'][0]['Title'])