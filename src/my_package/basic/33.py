"""
loop -> recebe valor -> valida valor -> chama função  -> printa
valor
"""

from my_package.clear import clear
from my_package.verify_and_convert import verify_float


def convert_r_to_s(real: float) -> float:
    base: float = 5.04
    dolar: float = real / base
    return dolar


while True:
    clear()
    a = input("Digite a quantidade de reais que você deseja converter: ")
    if verify_float(a):
        num = float(a)
        _result = convert_r_to_s(num)
        print(f"O valor do resultado da conversão é {_result} reais")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
