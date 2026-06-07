"""
básico:
-> recebe dois valores -> subtrai e eleva a subtração ao quadrado

simples:
loop -> recebe dois valores -> valida -> subtrai e eleva a subtração ao quadrado
"""

from my_package.clear import clear
from my_package.verify_and_convert import verify_int

# básico:
val1: int = int(input("Digite um número inteiro: "))
val2: int = int(input("Digite um segundo número inteiro: "))
result: int = (val1 - val2) ** 2
print(f"O quadrado da diferença é {result}")

input("Pressione enter para continuar...")
# simples:
while True:
    clear()
    print("O quadrado da diferença entre dois números")
    number = input("Digite um número inteiro: ")
    number2 = input("Digite um segundo número inteiro: ")
    if verify_int(number, number2):
        number, number2 = int(number), int(number2)
        result: int = (number - number2) ** 2
        print(f"O quadrado da diferença é {result}")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
