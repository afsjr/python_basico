lista = []
i=0
print('olá, seja bem vind@ !')
quant_convidados = int(input('quantos convidados teremos na festa ? '))
print('hummmm, interessante')

while i < quant_convidados:
    nome = input('nome do convidado ')
    lista.append(nome)
    i+=1

for i in lista:
    print(i)