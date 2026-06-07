"""
loop -> recebe os valores do usuário -> valida -> chama a função -> exibe
resultado
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float


def reajuste(num1: float, num2: float) -> float:
    porcent: float = num1 / 100
    salario: float = (num2 * porcent) + num2

    return salario


while True:
    clear()
    print("Iremos realiar o calculo do reajuste salarial")
    number1: str = input("Digite o porcentual: ")
    number2: str = input("Digite o valor do salário: ")
    if verify_float(number1, number2):
        nums: list[float] = convert_float(number1, number2)
        _result: float = reajuste(nums[0], nums[1])
        print(
            f"O salário de {nums[1]} terá um reajuste"
            f" de {nums[0]} porcentos e passará a ser {_result:.2f}"
        )
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
