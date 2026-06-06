'''
loop -> recebe dois valores -> valida -> subtrai e eleva a subtração ao quadrado
'''

from my_package.clear import clear
while True:
    clear()
    print("O quadrado da diferença entre dois números")
    number = input("Digite um número inteiro: ")
    number2 = input("Digite um segundo número inteiro: ")
    try:
        number, number2 = int(number), int(number2)

        result = (number - number2)**2
        print(f'O quadrado da diferença é {result}')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")