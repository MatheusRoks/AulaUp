from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa a formula
4*l e l**3
 -> mostra resultado
"""
while True:
    clear()
    print("Perimetro e area de um quadrilátero")
    lar: str = input("Digite o lado do quadrilátero: ")
    if verify_float(lar):
        nums = convert_float(lar)
        print(f"Perimetro do quadrilátero: {4 * nums[0]}")
        print(f"Area do quadrilátero: {nums[0] ** 3}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
