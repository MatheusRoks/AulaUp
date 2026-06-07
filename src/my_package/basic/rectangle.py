"""
loop -> recebe 3 valores -> valida -> multiplica eles
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

while True:
    clear()
    print("Calculo do volume de um paralelepipedo")
    c: str = input("Digite o comprimento: ")
    lar: str = input("Digite a lergura: ")
    h: str = input("Digitea altura: ")
    if verify_float(c, lar, h):
        nums = convert_float(c, lar, h)

        result: float = nums[0] * nums[1] * nums[2]
        print(f"O volume é {result:.2f}")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
