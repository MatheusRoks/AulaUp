from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe peso e altura -> verifica -> converte -> calcula IMC -> mostra resultado
"""
while True:
    clear()
    peso: str = input("Peso (kg): ")
    altura: str = input("Altura (m): ")

    if verify_float(peso, altura):
        nums = convert_float(peso, altura)
        imc: float = nums[0] / (nums[1] ** 2)
        print(f"IMC: {imc:.2f}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
