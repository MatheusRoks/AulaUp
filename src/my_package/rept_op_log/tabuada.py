from clear import clear
while True:
    clear()
    number = input("Digite um número INTEIRO: ")
    try:
        number = int(number)
        for i in range(11):
            y = number*i
            print(f"{number} x {i} = {y}")
        break
    except:
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")

