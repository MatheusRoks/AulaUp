from my_package.clear import clear

"""
recebe dias -> verifica -> converte
calcula semanas e dias restantes -> mostra resultado
"""

while True:
    clear()

    dias: str = input("Quantidade de dias: ")
    if dias.isdigit():
        _dias: int = int(dias)
        semanas = _dias // 7
        dias_restantes = _dias % 7
        print(f"Semanas: {semanas}")
        print(f"Dias restantes: {dias_restantes}")
        break

    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
