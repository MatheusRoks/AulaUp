"""
loop -> recebe os valores do usuário -> valida -> chama a função -> exibe
resultado

"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float


def cal_quad(num1: float, num2: float, num3: float) -> float:
    _result: float = (num1**2) + (num2**2) + (num3**2)
    return _result


while True:
    clear()
    print("Informe três números e irei realizar a soma do quadrado dos valores")
    number1: str = input("Digite o primeiro número: ")
    number2: str = input("Digite o segundo número: ")
    number3: str = input("Digite o terceiro número: ")
    if verify_float(number1, number2, number3):
        converted = convert_float(number1, number2, number3)
        _result = cal_quad(converted[0], converted[1], converted[2])
        print(
            f"A soma do quadrado dos valores: {number1}, {number2} e {number3}"
            f" é {_result}"
        )
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
