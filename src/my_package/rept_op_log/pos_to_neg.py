from my_package.clear import clear

"""
recebe valor -> valida -> converte -> se maior q 0 multiplica por -1 do contrario
apresenta o proprio valor
"""
while True:
    clear()
    number = input("Digite um número: ")
    try:
        number = float(number)
        if number > 0:
            number = number * -1
            print(f"o número convertido a negativo {number}")
        else:
            print(f"O número {number} já é negativo ou zero")
        break
    except (ValueError, TypeError):
        print("Valor inválido, favor digitar um númmero")
        input("Presione 'enter' para continuar")
