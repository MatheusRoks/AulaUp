from my_package.clear import clear

"""reeccbe -> verifica -> resultado"""
while True:
    clear()
    number = input("Digite um número INTEIRO: ")
    try:
        number = int(number)
        if number > 3:
            print(f"O valor {number} é maior que três")
        break
    except ValueError:
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")
