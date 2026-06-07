from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> x-y -> mostra resultado
"""
while True:
    clear()
    custo: str = input("Vamlor da compra: ")
    pagamento: str = input("Pagamento: ")
    if verify_float(custo, pagamento):
        nums: list[float] = convert_float(custo, pagamento)
        troco = nums[1] - nums[0]
        if troco >= 0:
            print(f"O troco é {troco:.2f}")
            break
        else:
            print("Insuficiente")
            input("enter para continuar")
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
