from clear import clear


while True:
    clear()
    print("Iremos realizar a média e a aprovação dos alunos.")
    med = 0
    for i in range(4):
        a = input("Digite uma nota: ")
        try:
            a = float(a)
            med +=a
        except:
            print("Valores informados inconsistentes, encerrando o programa")
            input("Aperte enter para continuar...")
            break       
    
    media = med/4

    if media>=7:
        print(f'Média {media}, Aprovado')
        break
    else:
        print(f'Média {media}, reprovado')
