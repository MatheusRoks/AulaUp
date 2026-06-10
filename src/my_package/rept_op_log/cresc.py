from my_package.clear import clear

"""
adicona os valores recebido dentro de uma lista ->usa sort ->printa

"""

while True:
    clear()

    print("Irei receber 3 números e ordená-los")

    try:
        numeros = [
            float(input("Digite o 1º número: ")),
            float(input("Digite o 2º número: ")),
            float(input("Digite o 3º número: ")),
        ]
        numeros.sort()
        print(numeros)
        break
    except ValueError:
        print("Valor inválido, favor digitar um número")
        input("Pressione Enter para continuar")


"""
recebe 3 valores, testa o 1 com o 2, se maiores, trocam de lugar.
testa  o 2 com o 3, se maiores, trocam de lugar.
Por ultimo testa novamente o primeiro e o segundo
"""
a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")
c = input("Digite o tereceiro número: ")

if a > b:
    b, a = a, b

if b > c:
    c, b = b, c

if a > b:
    b, a = a, b

print(f"{a}, {b}, {c}")
