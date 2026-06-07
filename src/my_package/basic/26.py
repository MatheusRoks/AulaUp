from my_package.clear import clear
from my_package.verify_and_convert import convert_int, verify_int

"""
recebe valor -> verifica se é int -> converte para int -> div int resto div ->
 mostra resultado
"""
while True:
    clear()
    print("Divisão inteira e resto de divisão")
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    if verify_int(num1, num2):
        nums = convert_int(num1, num2)
        resultado_div = nums[0] // nums[1]
        resultado_resto = nums[0] % nums[1]
        print(
            f"A divisão inteira de {nums[0]} por {nums[1]} é {resultado_div}"
            f" e o resto é {resultado_resto}."
        )
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
