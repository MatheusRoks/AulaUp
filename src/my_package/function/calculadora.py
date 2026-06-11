import op

from my_package.clear import clear
from my_package.utils import cyan_print, green_print, yellow_print

while True:
    yellow_print("===================Calculadora cientifica===================")
    print(
        "Opções:\n"
        "1 = Soma\n"
        "2 = Subtração\n"
        "3 = Fatorial\n"
        "4 = Multiplicação\n"
        "5 = Divisão\n"
        "6 = Potência\n"
        "7 = Raiz quadrada\n"
        "8 = Raiz cúbica\n"
        "9 = Número primo\n"
        "10 = Verificar múltiplo\n"
        "11 = Verificar divisor\n"
        "12 = MDC\n"
        "13 = MMC\n"
        "14 = Média\n"
        "15 = Maior número\n"
        "16 = Menor número\n"
        "17 = Bhaskara\n"
        "18 = Pitágoras\n"
    )
    option: str = input("Digite a opção que deseja selecionar: ")
    clear()

    match option:
        case "1":
            green_print("Soma selecionada")
            cyan_print(op.soma())
        case "2":
            green_print("Subtração selecionada")
            cyan_print(op.sub())
        case "3":
            green_print("Fatorial selecionado")
            cyan_print(op.fatorial())
        case "4":
            green_print("Multiplicação selecionada")
            cyan_print(op.mult())
        case "5":
            green_print("Divisão selecionada")
            cyan_print(op.div())
        case "6":
            green_print("Potência selecionada")
            cyan_print(op.pot())
        case "7":
            green_print("Raiz quadrada selecionada")
            cyan_print(op.raiz())
        case "8":
            green_print("Raiz cúbica selecionada")
            cyan_print(op.raizcub())
        case "9":
            green_print("Número primo selecionado")
            cyan_print(op.numprim())
        case "10":
            green_print("Verificação de múltiplo selecionada")
            cyan_print(op.ismult())
        case "11":
            green_print("Verificação de divisor selecionada")
            cyan_print(op.isdivisor())
        case "12":
            green_print("MDC selecionado")
            cyan_print(op.mdc())
        case "13":
            green_print("MMC selecionado")
            cyan_print(op.mmc())
        case "14":
            green_print("Média selecionada")
            cyan_print(op.media())
        case "15":
            green_print("Maior número selecionado")
            cyan_print(op.maior())
        case "16":
            green_print("Menor número selecionado")
            cyan_print(op.menor())
        case "17":
            green_print("Bhaskara selecionada")
            cyan_print(op.bhask())
        case "18":
            green_print("Pitágoras selecionado")
            cyan_print(op.pitagoras())
        case _:
            break
