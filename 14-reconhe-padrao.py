import re

string_de_teste = 'o gato, a gata, os gatos, as gatinhas e os gatoes'

padrao = re.findall(r'gat\w*',string_de_teste)

if padrao:
    print(padrao)
else:
    print('padrao não encontrado')