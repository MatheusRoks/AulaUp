from my_package.clear import clear
from my_package.verify_num import convert_float, verify_float

"""
O código funciona da seguinte forma:
    um laço de repetição, dentro desse laço a principio um print informando o
    que a função faz é executado. Ao infromar o valor ele tenta converter, caso
    seja possivel o laço é interrompido. caso não, emite uma mensagem de erro e
    inicia novamente o laço para um novo numero ser inserido

    a unica diferença entre o modo simples e o modo básico é a verificação dos dados. 
    no basico isso é ignorado
"""
gcelcius = input("Digite o valor em Celcius a ser convertido: ")
fahrenheit = (float(gcelcius) * 1.8) + 32
print(f'{gcelcius} celcius equivale a {fahrenheit:.2f} em fahrenheit')

input("Pressione enter para continuar...")

while True:
    clear()
    print("Vamos converter a temperatura de Celcius para Fahrenheit.") 
    celsius:str = input("Digite o valor em Celcius a ser convertido: ")
    if verify_float(celsius):
        nums = convert_float(celsius)
        fahrenheit:float = (nums[0] * 1.8) + 32
        print(f'{celsius} celcius equivale a {fahrenheit:.2f} em fahrenheit')
        break
    else:
        print("O valor informado não pode ser convertido")
        input("Aperte enter para continuar...")
