#este programa tem o intuito de descobrir quais os números primos de uma sequencia informada pelo usuário

if __name__ == '__main__':
    num1 = -1

    try:
        while num1<0: # objetivo manter o programa funcionando enquanto a pessoa não digitar um número positivo
            primos = []
            nprimos = []
            num1 = int(input('Escolha um número para verificar se ele é primo ou nao: '))
            for i in range(num1+1): # percorrer a lista de todos os números do zaro até o valor escolhido e separa quais são primos ou não.
              if i == 2 or i == 3 or i == 5 or i == 7:
                primos.append(i)
              elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                nprimos.append(i)
              else:
                primos.append(i)

            print('são números primos -> ', primos)
            print('não são números primos -> ',nprimos)

    except ValueError:
        print('É preciso digitar um número inteiro positivo . Tente outra vez')