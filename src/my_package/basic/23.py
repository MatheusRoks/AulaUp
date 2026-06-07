from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa
(x*y)+y-> mostra resultado
"""
while True:
    clear()
    prest: str = input("Digite o valor da prestação atrasada: ")
    juros: str = input("Digite o valor dos juros por atraso(j/m): ")
    atrasos: str = input("Tempo que está atrasada(meses): ")
    if verify_float(prest, juros, atrasos):
        nums: list[float] = convert_float(prest, juros, atrasos)
        resultado = nums[0] + (nums[1] * nums[2])
        print(f"O novo valor a ser pago é {resultado:.2f}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
