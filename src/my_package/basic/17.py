"""
recebe um número inteiro -> valida -> converte -> subtrai um: printa antecessor->
adiciona um: printa sucessor
"""

from my_package.clear import clear

while True:
    clear()
    number1: str = input("Digite um número inteiro: ")
    if number1.isdigit():
        number: int = int(number1)
        print(f"Antecessor: {number - 1}")
        print(f"Sucessor: {number + 1}")
        break
    else:
        print("Valor inválido. Tente novamente.")
        input("Pressione Enter para continuar...")
