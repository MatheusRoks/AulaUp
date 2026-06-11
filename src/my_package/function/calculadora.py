import op

from my_package.clear import clear
from my_package.utils import cyan_print, green_print, yellow_print

while True:
    clear()
    yellow_print("===================Calculadora cientifica===================")
    print(
        f"{'1 = Soma':<25}{'10 = Verificar múltiplo'}\n"
        f"{'2 = Subtração':<25}{'11 = Verificar divisor'}\n"
        f"{'3 = Fatorial':<25}{'12 = MDC'}\n"
        f"{'4 = Multiplicação':<25}{'13 = MMC'}\n"
        f"{'5 = Divisão':<25}{'14 = Média'}\n"
        f"{'6 = Potência':<25}{'15 = Maior número'}\n"
        f"{'7 = Raiz quadrada':<25}{'16 = Menor número'}\n"
        f"{'8 = Raiz cúbica':<25}{'17 = Bhaskara'}\n"
        f"{'9 = Número primo':<25}{'18 = Pitágoras'}"
    )
    option: str = input("Digite a opção que deseja selecionar: ")
    clear()

    match option:
        case "1":
            green_print("Soma selecionada")
            cyan_print(op.soma())
            input("Enter para continuar")
        case "2":
            green_print("Subtração selecionada")
            cyan_print(op.sub())
            input("Enter para continuar")
        case "3":
            green_print("Fatorial selecionado")
            cyan_print(op.fatorial())
            input("Enter para continuar")
        case "4":
            green_print("Multiplicação selecionada")
            cyan_print(op.mult())
            input("Enter para continuar")
        case "5":
            green_print("Divisão selecionada")
            cyan_print(op.div())
            input("Enter para continuar")
        case "6":
            green_print("Potência selecionada")
            cyan_print(op.pot())
            input("Enter para continuar")
        case "7":
            green_print("Raiz quadrada selecionada")
            cyan_print(op.raiz())
            input("Enter para continuar")
        case "8":
            green_print("Raiz cúbica selecionada")
            cyan_print(op.raizcub())
            input("Enter para continuar")
        case "9":
            green_print("Número primo selecionado")
            cyan_print(op.numprim())
            input("Enter para continuar")
        case "10":
            green_print("Verificação de múltiplo selecionada")
            cyan_print(op.ismult())
            input("Enter para continuar")
        case "11":
            green_print("Verificação de divisor selecionada")
            cyan_print(op.isdivisor())
            input("Enter para continuar")
        case "12":
            green_print("MDC selecionado")
            cyan_print(op.mdc())
            input("Enter para continuar")
        case "13":
            green_print("MMC selecionado")
            cyan_print(op.mmc())
            input("Enter para continuar")
        case "14":
            green_print("Média selecionada")
            cyan_print(op.media())
            input("Enter para continuar")
        case "15":
            green_print("Maior número selecionado")
            cyan_print(op.maior())
            input("Enter para continuar")
        case "16":
            green_print("Menor número selecionado")
            cyan_print(op.menor())
            input("Enter para continuar")
        case "17":
            green_print("Bhaskara selecionada")
            cyan_print(op.bhask())
            input("Enter para continuar")
        case "18":
            green_print("Pitágoras selecionado")
            cyan_print(op.pitagoras())
            input("Enter para continuar")
        case _:
            break
