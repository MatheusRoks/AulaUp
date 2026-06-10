from my_package.clear import clear

"""recebe numero, laço, multiplicação do numero recebido exibiçãoo"""
i = 0
while True:
    clear()
    number = input("Digite um número INTEIRO: ")
    try:
        number = int(number)
        while i <= 9:
            i += 1
            y = number * i
            print(f"{number} x {i} = {y}")
        break
    except ValueError:
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")
