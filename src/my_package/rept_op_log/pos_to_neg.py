from clear import clear
while True:
    clear()
    number = input("Digite um número: ")
    try:
        number = float(number)
        if number>=0:
            number = number*-1
            print(f'o número convertido a negativo {number}')
        else:
            print(f'O número {number} já é negativo')
        break
    except:
        print("Valor inválido, favor digitar um númmero")
        input("Presione 'enter' para continuar")