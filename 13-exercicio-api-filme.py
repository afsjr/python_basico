import requests
import json

def listafilmes(titulo):
    lista = []
    for i in range(1,100):
        print(i)
        try:
            req = requests.get('https://www.omdbapi.com/?apikey=25ddb129&s=' + titulo + '&type=movie&page='+str(i))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + ' (' + ano + ' )'
                    lista.append(string)
            else:
                print('fim das páginas')
                break
        except:
            print('falha na conexão !!!!')
    return lista

sair = False
while not sair:
    filme = input('Digite o nome do filme para pesquisa ou SAIR : ')
    if filme == 'SAIR':
        sair == True
        break
    else:
       filmes_encontrados= listafilmes(filme)
       print('filmes encontrados', len(filmes_encontrados))
       for filme in filmes_encontrados:
           print(filme)

    print('Total de filmes encontrados = ', len(filmes_encontrados))