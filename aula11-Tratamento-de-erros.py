import time

def abre_arquivo():
    try :
        open('arquivodoid.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro:', erro)
        return False


while not abre_arquivo():
    print('tentando abrir o arquivo')
    time.sleep(5)

print('consegui abrir o aquivo')
