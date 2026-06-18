from my_package.classes.diario_classe.turma import Turma


def main() -> None:
    turma = Turma()

    while True:
        print("\nDiário")
        print("1 - Matricular Aluno")
        print("2 - Lançar Nota")
        print("3 - Exibir Boletim")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                turma.matricular()
            case "2":
                turma.lancar_nota()
            case "3":
                turma.exibir_boletim()
            case "4":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
