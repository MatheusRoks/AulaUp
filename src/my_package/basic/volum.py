"""
básico:
usuário insere os dados, já são convertidos e atribuidos a váriávies ->
calcula volume do cilindro ->print resultado.

simples:
laço de repetição -> usuário insere os dados ->
verificação dos dados -> pi * r**2 * altura -> valor
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

# básico:
raio: float = float(input("Informe o valor do raio: "))
altura: float = float(input("Informe o valor da altura: "))
PI: float = 3.1415
volume: float = PI * (raio**2) * altura
print(
    f"Para um cilindro com {raio} de raio e {altura} de altura, temos"
    f" {volume:.2f} de volume"
)

# simples:

while True:
    clear()
    print("cálculo do volume do cilindro")
    r: str = input("Informe o valor do raio: ")
    h: str = input("Informe o valor da altura")

    if verify_float(r) and verify_float(h):
        nums = convert_float(r, h)
        vol = PI * (nums[0] ** 2) * nums[1]
        print(
            f"Para um cilindro com {r} de raio e {h} de altura, temos {vol:.2f}"
            f"de volume"
        )
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
