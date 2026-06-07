"""
loop -> recebe os valores do usuário -> valida -> realiza as operações -> exibe
resultado
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_int, verify_int

while True:
    clear()
    print("Iremos realiar  e a soma de 2 números")
    number1 = input("Digite o primeiro número: ")
    number2 = input("Digite o segundo número: ")
    if verify_int(number1, number2):
        nums: list[int] = convert_int(number1, number2)
        multi = nums[0] * nums[1]
        soma = nums[0] + nums[1]
        print(f"O resultado da multiplicação de {nums[0]} e {nums[1]} é {multi}")
        print(f"O resultado da soma de {nums[0]} e {nums[1]} é {soma}")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
