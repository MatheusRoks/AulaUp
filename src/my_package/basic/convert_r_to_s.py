"""
loop -> recebe valor -> valida valor -> chama função (faz piadinha) -> printa 
valor
"""
from my_package.clear import clear

def convert_r_to_s(dolar:float):
    BASE = 5.04
    real = dolar * BASE
    return real

while True:
    clear()
    a = input("Digite a quantidade de dólar que você deseja converter: ")
    try:
        a = float(a)
        _result = convert_r_to_s(a)
        real_value = _result - (_result * 0.10)
        print(f'O valor do resultado da conversão é {_result} reais')
        print(f'Mas como é o Brasil, só vai receber {real_value:.2f} reais')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")