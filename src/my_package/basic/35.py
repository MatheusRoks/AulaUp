from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa: km/litros
 -> mostra resultado
"""
while True:
    clear()
    print("Cálculo do consumo de litros/km")
    dis: str = input("Digite distancia: ")
    litros: str = input("Digite quantidade de litros consumido): ")
    if verify_float(dis, litros):
        nums = convert_float(dis, litros)
        consum_med: float = nums[0] / nums[1]
        print(f"O consumo médio de km/l é {consum_med}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
