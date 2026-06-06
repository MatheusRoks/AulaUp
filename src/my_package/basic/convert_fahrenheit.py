"""
O código funciona da seguinte forma:
    um laço de repetição, dentro desse laço a principio um print informando o
    que a função faz é executado. Ao infromar o valor ele tenta converter, caso
    seja possivel o laço é interrompido. caso não, emite uma mensagem de erro e
    inicia novamente o laço para um novo numero ser inserido
"""
from my_package.clear import clear
while True:
    clear
    print("Vamos converter a temperatura de fahrenheit para Celsius.")
    fahrenheit = input("digite uma temperatura em fahrenheit: ")
    try:
        fahrenheit:float = float(fahrenheit)
        celsius:float = (fahrenheit-32)/1.8
        print(f'{fahrenheit} fahrenheit equivale a {celsius:.2f} Celsius')
        break
    except:
        print("Valor informado  não pode ser convertido")
        input("Aperte enter para continuar...")
