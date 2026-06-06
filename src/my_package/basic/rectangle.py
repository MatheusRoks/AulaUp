'''
loop -> recebe 3 valores -> valida -> multiplica eles
'''

from my_package.clear import clear
while True:
    clear()
    print("Calculo do volume de um paralelepipedo")
    c:float = input("Digite o comprimento: ")
    l:float = input("Digite a lergura: ")
    h:float = input("Digitea altura: ")
    try:
        c, l, h= float(c), float(l), float(h)

        result = c*l*h
        print(f'O volume é {result:.2f}')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")