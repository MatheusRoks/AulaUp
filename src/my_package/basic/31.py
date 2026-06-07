from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa
salario + (vendas*comissão) -> mostra resultado
"""
while True:
    clear()
    salario: str = input("Digite o salário fixo: ")
    vendas: str = input("Total de vendas: ")
    comissao: str = input("Porcentagem da comissão")
    if verify_float(salario, vendas, comissao):
        nums: list[float] = convert_float(salario, vendas, comissao)
        porcento: float = nums[2] / 100
        print(f"O salário final é de {(nums[0] + (nums[1] * porcento)):.2f}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
