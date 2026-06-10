from my_package.clear import clear

"""recebe valor->ve se é maior ou igual a um e menor ou igual a nove -> se sim
dentro, senão, fora"""
while True:
    clear()
    number = input("Digite um número INTEIRO: ")
    try:
        number = int(number)
        if number >= 1 and number <= 9:
            print(f"O valor {number} se encontra dentro do intervalo de 1 a 9")
        else:
            print("O valor informado não se encontra no intervalo")
        break
    except ValueError:
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")
