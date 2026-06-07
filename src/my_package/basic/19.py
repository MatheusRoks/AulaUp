from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> multiplica pela
constante -> mostra resultado
"""
while True:
    clear()
    print("Converter idade de anos para dias")
    age = input("Digite sua idade em anos: ")
    DAYS = 365
    if verify_float(age):
        nums = convert_float(age)
        print(f"Valor em dias: {nums[0] * DAYS}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
