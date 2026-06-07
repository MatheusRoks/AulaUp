from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
--------------básico-------------
lógica: input do valor em celsius -> calculo E conversão do dado (converte o
input para float * 1.8 + 32) -> print do resultado

---------simples-------------------
laço de repetição -> limpa o terminar -> print do sistema explicando a função
-> input de dados -> verificação do dado -> se valido, convertido, calculado
printa o resultado e quebra o laço -> se inválido, printa mensagem de erro e
pede para continuar
"""
gcelcius: str = input("Digite o valor em Celcius a ser convertido: ")
fahrenheit: float = (float(gcelcius) * 1.8) + 32
print(f"{gcelcius} celcius equivale a {fahrenheit:.2f} em fahrenheit")

input("Pressione enter para continuar...")

while True:
    clear()
    print("Vamos converter a temperatura de Celcius para Fahrenheit.")
    celsius: str = input("Digite o valor em Celcius a ser convertido: ")
    if verify_float(celsius):
        nums = convert_float(celsius)
        fahrenheit: float = (nums[0] * 1.8) + 32
        print(f"{celsius} celcius equivale a {fahrenheit:.2f} em fahrenheit")
        break
    else:
        print("O valor informado não pode ser convertido")
        input("Aperte enter para continuar...")
