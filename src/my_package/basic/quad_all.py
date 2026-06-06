"""
loop -> recebe os valores do usuário -> valida -> chama a função -> exibe 
resultado

"""



from my_package.clear import clear

def cal_quad(num1:float, num2:float, num3:float):
    _result = (num1**2)+(num2**2)+(num3**2)
    return _result


while True:
    clear()
    print("Informe três números e irei realizar a soma do quadrado dos valores")
    number1 = input("Digite o primeiro número: ")
    number2 = input("Digite o segundo número: ")
    number3 = input("Digite o terceiro número: ")
    try:
        number1, number2, number3 = float(number1), float(number2), float(number3)
        _result = cal_quad(number1, number2, number3)
        print(f'A soma do quadrado dos valores: {number1}, {number2} e {number3} é {_result}')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")