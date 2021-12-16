import requests
import json

def requisicao(titulo):
    try:
        req = requests.get('https://www.omdbapi.com/?apikey=25ddb129&s='+ titulo +'&type=movie')
        print(req.text)
    except:
        print('falha na conexão !!!!')

requisicao('interstellar')