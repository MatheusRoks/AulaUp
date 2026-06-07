from my_package.clear import clear

"""
recebe valor -> verifica se é float -> converte para float -> executa x^y ->
mostra resultado
"""
while True:
    clear()
    print("Calcula x^y")
    x: str = input("Digite o primeiro valor: ")
    y: str = input("Digite o segunndo valor: ")
    if x.isdigit() and y.isdigit():
        print(f"{x} elevado a {y} = {(int(x) ** int(y))}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
