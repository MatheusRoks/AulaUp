"""
recebe 3 notas -> valida as notas -> converte as notas -> calcula a média ->
exibe o resultado
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float


def calc_media(n1: float, n2: float, n3: float) -> float:
    media: float = (n1 + n2 + n3) / 3
    return media


while True:
    clear()
    print("Cálculo da média de 3 notas")
    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    nota3 = input("Digite a terceira nota: ")
    if verify_float(nota1, nota2, nota3):
        for i in range(3):
            if i < 0 or i > 10:
                print("As notas devem ser entre 0 e 10")
                input("Pressione enter para nova tentativa")
                break
        nums: list[float] = convert_float(nota1, nota2, nota3)
        _result = calc_media(nums[0], nums[1], nums[2])
        print(f"A média das notas {nums[0]}, {nums[1]} e {nums[2]} é {_result:.2f}")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
