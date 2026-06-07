from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa (x*y)+z ->
mostra resultado
"""
while True:
    clear()
    print("Cálculo do valor final de um produto")
    custo: str = input("Digite o custo do produto: ")
    lucro: str = input("Digite a porcentagem de lucro desejado: ")
    if verify_float(custo, lucro):
        nums = convert_float(custo, lucro)
        porcentagem_lucro = nums[1] / 100
        resultado = (nums[0] * porcentagem_lucro) + nums[0]
        print(f"O valor final do produto é {resultado}.")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
