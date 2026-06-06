"""
loop -> recebe os valores do usuário -> valida -> chama a função -> exibe 
resultado
"""

from my_package.clear import clear

def mult_cal(num1:float, num2:float, num3:float, num4:float):
    _result_a = num1*num3
    _result_b = num2+num4
    
    return [_result_a, _result_b]


while True:
    clear()
    print("Iremos realiar a multiplicação do 3 e 1 valor e a soma do 2 com o 4")
    number1 = input("Digite o primeiro número: ")
    number2 = input("Digite o segundo número: ")
    number3 = input("Digite o terceiro número: ")
    number4 = input("Digite o quarto número: ")
    try:
        number1, number2, number3, number4 = float(number1), float(number2), float(number3), float(number4)
        _result = mult_cal(number1, number2, number3, number4)
        print(f'O resultado da multiplicação de {number3} e {number1} é {_result[0]}')
        print(f'O resultado da soma de {number2} e {number4} é {_result[1]}')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")