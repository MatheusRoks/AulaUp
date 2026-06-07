"""
--------------básico------------------
recebe e já converte o valor do fahrenheit para float > executa a formula de conversão
(x-32)/1.8 > print do resultado

--------------simples-----------------
laço de repetição -> limpa o terminal -> print do sistema explicando a função
-> input de dados -> verificação do dado -> se valido, convertido, calculado
printa o resultado e quebra o laço -> se inválido, printa mensagem de erro e
pede para continuar
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

# basico
bfahrenheit: float = float(input("Digite o valor em Fahrenheit a ser convertido: "))
celsius: float = (bfahrenheit - 32) / 1.8
print(f"{bfahrenheit} fahrenheit equivale a {celsius:.2f} em Celsius")

# simples
while True:
    clear()
    print("Vamos converter a temperatura de fahrenheit para Celsius.")
    fahrenheit: str = input("digite uma temperatura em fahrenheit: ")
    if verify_float(fahrenheit):
        nums: list[float] = convert_float(fahrenheit)
        celsius: float = (nums[0] - 32) / 1.8
        print(f"{fahrenheit} fahrenheit equivale a {celsius:.2f} em Celsius")
        break
    else:
        print("Valor informado  não pode ser convertido")
        input("Aperte enter para continuar...")
