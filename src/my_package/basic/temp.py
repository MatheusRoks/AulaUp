from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> multiplica pela
constante -> mostra resultado
"""
while True:
    clear()
    if verify_float():
        convert_float()
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
