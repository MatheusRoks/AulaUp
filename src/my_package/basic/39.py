from my_package.clear import clear

"""
recebe valor -> verifica se é float -> converte para float -> executa x*y ->
mostra resultado
"""
while True:
    clear()
    print("Calcula total")
    x: str = input("Digite a qauntidade comprada: ")
    y: str = input("Digite o valor unitário: ")
    if x.isdigit() and y.isdigit():
        print(f"o total é = {(int(x) * int(y))}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
