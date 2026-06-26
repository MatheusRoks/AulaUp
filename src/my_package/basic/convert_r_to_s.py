"""
loop -> recebe valor -> valida valor -> chama função (faz piadinha) -> printa
valor
"""

from my_package.clear import clear
from my_package.verify_and_convert import verify_float


def convert_r_to_s(dolar: float) -> float:
    base: float = 5.04
    real: float = dolar * base
    return real


while True:
    clear()

    a = input("Digite a quantidade de dólar que você deseja converter: ")
    
    if verify_float(a):
        num = float(a)
        _result = convert_r_to_s(num)
        real_value = _result - (_result * 0.10)
        print(f"O valor do resultado da conversão é {_result} reais")
        print(f"Mas como é o Brasil, só vai receber {real_value:.2f} reais")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
