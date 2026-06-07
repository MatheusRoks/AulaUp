from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> multiplica hora pelo
valor -> mostra resultado
"""
while True:
    clear()
    print("Calcular o valor a pagar por horas trabalhadas")
    vlh: str = input("Digite o valor da hora trabalhada: ")
    hr: str = input("Digite a quantidade de horas trabalhadas: ")
    if verify_float(vlh, hr):
        nums = convert_float(vlh, hr)
        print(f"Valor a pagar: {(nums[0] * nums[1]):.2f}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
