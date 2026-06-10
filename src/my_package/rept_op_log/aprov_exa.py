from my_package.clear import clear

while True:
    clear()
    print("Iremos realizar a média e a aprovação dos alunos.")
    med = 0
    for i in range(4):
        i = 0
        a = input("Digite uma nota: ")
        try:
            a = float(a)
            med += a
        except (TypeError, ValueError):
            print("Valores informados inconsistentes, encerrando o programa")
            input("Aperte enter para continuar...")
            break

    media = med / 4

    if media >= 7:
        print(f"Média {media}, Aprovado")
        break
    else:
        print(f"Média {media}, reprovado")
        print("Exame final solicitado")
        a = input("Digite a nota do exame final: ")
        try:
            a = float(a)
            if a > 10:
                print("Valor inválido, encerrando o programa")
                break
            else:
                if a < 5:
                    print("Aluno reprovado no exame final")
                    break
                else:
                    print("Aluno aprovado no exame final")
                    break
        except (TypeError, ValueError):
            print("Valores informados inválidos, encerrando o programa")
            break
