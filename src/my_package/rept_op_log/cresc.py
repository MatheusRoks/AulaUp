from clear import clear

while True:
    clear()
    print("Irei reber 3 números e ordená-los")
    a = input("Digite o 1º número: ")
    b= input("Digite o 2º número: ")
    c = input("Digite o 3º número: ")
    lista_num = []
    try:
        a,b,c = float(a), float(b), float(c)
        lista_num.append(a)
        lista_num.append(b)
        lista_num.append(c)
        lista_num.sort()
        print(lista_num)
        break
    except:
        print("Valor inválido, favor digitar um númmero")
        input("Presione 'enter' para continuar")