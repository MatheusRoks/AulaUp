# recebe umm número inteiro -> eleva o número ao quadrado -> exibe o resultado.
from my_package.clear import clear

num = int(input("Digite um número inteiro: "))
print(f"O quadrado de {num} é {num**2}")

input("Pressione enter para continuar...")
while True:
    clear()
    print("Iremos exibiro quadrado de um numero inteiro")
    num2: str = input("Digite um número inteiro: ")
    if num2.isdigit():
        num2_c = int(num2)
        print(f"O quadrado de {num2_c} é {num2_c**2}")
        break
    else:
        print("O valor informado não é um número inteiro")
        input("Pressione enter para nova tentativa")
