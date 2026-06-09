from my_package.utils import yellow_print, cyan_print, green_print
import op
from my_package.clear import clear
while True:
    yellow_print("===================Calculadora cientifica===================")
    print(
        f'Opções:\n'
        f'1 = Soma\n'
        f'2 = Subtração\n'
          )
    option:str = input("Digite a opção que deseja selecionar: ")
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
            

        case _:
            break