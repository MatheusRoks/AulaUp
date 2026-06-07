from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> multiplica pela
constante -> mostra resultado
"""
while True:
    clear()
    print("kg para g")
    G: int = 1000
    kg: str = input("Digite quilo: ")
    if verify_float(kg):
        num = convert_float(kg)
        print(f"O resultado da conversão é{(num[0] * G):.0f}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
