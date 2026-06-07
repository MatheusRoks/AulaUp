from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> multiplica pela
constante -> mostra resultado
"""

MESES: int = 12
while True:
    clear()
    print("Anos em meses")
    anos: str = input("Digite a quantidade de anos: ")
    if verify_float(anos):
        num_anos: list[float] = convert_float(anos)
        resultado: float = num_anos[0] * MESES
        print(f"{num_anos[0]} anos equivalem a {resultado:.0f} meses.")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
