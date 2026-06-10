"""recebe um numero -> verifica se é não é divisivel por nada ->
verifica se é divisivel por ambos -> verifica se é só por 2
verifica se é por 3.

abre excessão e caso de erro
"""

a = 0
while a < 4:
    number = input("Digite um número INTEIRO: ")
    try:
        number = int(number)
        if number % 2 != 0 and number % 3 != 0:
            print(f"O valor {number} não divisivel por 2 e/ou 3")
        elif number % 2 == 0 and number % 3 == 0:
            print(f"O valor {number} é divisivel por 2 e 3")
        elif number % 2 == 0:
            print(f"O valor {number} é divisivel por 2")
        else:
            print(f"O valor {number} é divisivel por 3")
        a += 1
    except (ValueError, TypeError):
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")
