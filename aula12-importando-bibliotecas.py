import requests

try:
    requisicao = requests.get('https://solyd.com.br')

except Exception as erro:
    print('solicitação apresentou erro : ', erro)

print(requisicao.text)
