#Refazendo uma calculadora

soma = lambda num1,num2 : num1+num2
subtracao = lambda num1,num2: num1-num2
multiplica = lambda num1, num2: num1*num2
divisao = lambda num1,num2 :num1/num2
choice =0

while choice>4 or choice <1:
    choice = int(input('qual a operaçao que deseja realizer ? \n1-soma\n2-subtraçao\n3-multiplicação\n4-divisao\n(1/2/3/4) : '))
    num1 = float(input('primeiro número: '))
    num2 = float(input('segundo número: '))
    if choice == 1 : print('soma de',num1,'+',num2,'= ',soma(num1,num2))
    elif choice == 2 : print('subtração de',num1,'+',num2,'= ',subtracao(num1,num2))
    elif choice == 3 : print('multiplicação de',num1,'+',num2,'= ',multiplica(num1,num2))
    else: print('divisao de',num1,'+',num2,'= ',divisao(num1,num2))


