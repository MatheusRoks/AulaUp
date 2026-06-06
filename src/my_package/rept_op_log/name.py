from clear import clear
while True:
    clear()
    name:str = input("Digite seu nome: ")
    sex = input("Digite seu sexo (M ou F): ")
    try:
        if not name.isalpha():
            input("Valor para nome inválido, pressione enter para continuar")
            continue
        sex = sex.upper()
        if sex not in ['M','F']:
            print("Valor informado para sexo inválido, favor digitar M ou F")
            input("Presione 'enter' para continuar")
            continue

        elif sex =='M':
            print(f'Ilmo. Sr. {name}')
        else:
            print(f'Ilma. Sra. {name}')
        break
    except:
        print("Valor inválido, favor digitar algo válido")
        input("Presione 'enter' para continuar")

