from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> divide  pela
constante (divisão exata, horas)-> resto da divisão(minutos)-> mostra resultado
"""
while True:
    clear()
    print("Convertendo minutos para horas")
    minutos: str = input("Digite o valor em minutos: ")
    CONSTANTE: int = 60
    if verify_float(minutos):
        nums = convert_float(minutos)
        horas = nums[0] // CONSTANTE
        minutos_restantes = nums[0] % CONSTANTE
        print(
            f"{nums[0]} minutos equivalem a {horas:.0f} horas e {minutos_restantes:.0f}"
            f" minutos."
        )
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
