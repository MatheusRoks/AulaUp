from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa a formula(l+h)*2
 -> mostra resultado
"""
while True:
    clear()
    print("Perimetro de um retangulo")
    lar: str = input("Digite a largura do retangulo: ")
    h: str = input("Digite a altura do retangulo: ")
    if verify_float(lar, h):
        nums = convert_float(lar, h)
        print(f"Perimetro do retangulo: {2 * (nums[0] + nums[1])}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
