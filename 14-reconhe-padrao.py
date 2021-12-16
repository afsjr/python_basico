import re

string_de_teste = 'o gato é bonito'

padrao = re.search(r'\w\w\w\w',string_de_teste)

if padrao:
    print(padrao.group())
else:
    print('padrao não encontrado')