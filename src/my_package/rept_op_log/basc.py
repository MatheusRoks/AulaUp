import math

from my_package.clear import clear

"""
recebe os dados -> tenta converter -> executa a operação - resultados - >
em caso de erros, retorna o loop
"""
while True:
    clear()

    a: str = input("Digite o coeficiente A: ")
    b: str = input("Digite o coeficiente B: ")
    c: str = input("Digite o coeficiente C: ")
    try:
        a_int: int = int(a)
        b_int: int = int(b)
        c_int: int = int(c)
        form: int = (b_int**2) - (4 * a_int * c_int)
        if form >= 0:
            raiz: float = math.sqrt(form)
            print(f"A raiz de {form:.2f} é {raiz:.2f}")
        else:
            print(f"O valor {form:.2f} não é possivel extrair raíz")
        break
    except ValueError:
        opcao: str = input(
            "Os dados informados são inválidos, pressione enter para continuar"
            "ou N para sair"
        )
        if opcao.upper() == "N":
            break
