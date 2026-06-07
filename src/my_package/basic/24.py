from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> exevuta b*h/2
 -> mostra resultado
"""
while True:
    clear()
    print("Cálculo da área de um triângulo")
    h: str = input("Digite a altura do triângulo: ")
    b: str = input("Digite a base do triângulo: ")
    if verify_float(h, b):
        nums: list[float] = convert_float(h, b)
        resultado: float = nums[0] * nums[1] / 2
        print(f"A área do triângulo é {resultado:.2f}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
