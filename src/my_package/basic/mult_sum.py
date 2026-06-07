"""
loop -> recebe os valores do usuário -> valida -> chama a função -> exibe
resultado
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float


def mult_cal(num1: float, num2: float, num3: float, num4: float) -> list[float]:
    _result_a: float = num1 * num3
    _result_b: float = num2 + num4

    return [_result_a, _result_b]


while True:
    clear()
    print("Iremos realiar a multiplicação do 3 e 1 valor e a soma do 2 com o 4")
    number1 = input("Digite o primeiro número: ")
    number2 = input("Digite o segundo número: ")
    number3 = input("Digite o terceiro número: ")
    number4 = input("Digite o quarto número: ")
    if verify_float(number1, number2, number3, number4):
        nums: list[float] = convert_float(number1, number2, number3, number4)
        _result = mult_cal(nums[0], nums[1], nums[2], nums[3])
        print(f"O resultado da multiplicação de {nums[2]} e {nums[0]} é {_result[0]}")
        print(f"O resultado da soma de {nums[1]} e {nums[3]} é {_result[1]}")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
