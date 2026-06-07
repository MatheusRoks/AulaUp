from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> multiplica pela
constante -> mostra resultado
"""

while True:
    clear()
    print("Convertendo metro em centrimetros")
    CM: int = 100
    m: str = input("Digite o valor em metros: ")
    if verify_float(m):
        nums = convert_float(m)
        print(f"Valor em centímetros: {nums[0] * CM}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
