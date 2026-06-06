from clear import clear
while True:
    clear()
    number = input("Digite um número INTEIRO: ")
    try:
        number = int(number)
        if number%2==0 and number%3==0:
            print(f"O valor {number} é divisivel por 2 e 3")
        else:
            print(f'O valor {number} não é divisivel simultaneamente por 2 e 3')
        break
    except:
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")

