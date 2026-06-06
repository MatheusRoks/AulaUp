a = 0
while a<4:
    number = input("Digite um número INTEIRO: ")
    a+=1
    try:
        number = int(number)
        if number%2 != 0 and number%3!=0:
            print(f"O valor {number} não divisivel por 2 e/ou 3")
        elif number%2==0 and number%3==0:
            print(f"O valor {number} é divisivel por 2 e 3")
        elif number%2 == 0: 
            print(f"O valor {number} é divisivel por 2")
        else:
            print(f"O valor {number} é divisivel por 3")
    except:
        print("Valor inválido, favor digitar um número")
        input("Presione 'enter' para continuar")



