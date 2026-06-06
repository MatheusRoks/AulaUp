"""
loop -> recebe os valores do usuário -> valida -> chama a função -> exibe 
resultado
"""

from my_package.clear import clear

def reajuste(num1:float, num2:float):
    porcent = num1/100
    salario = (num2*porcent)+num2
    
    return salario


while True:
    clear()
    print("Iremos realiar o calculo do reajuste salarial")
    number1 = input("Digite o porcentual: ")
    number2 = input("Digite o valor do salário: ")
    try:
        number1, number2= float(number1), float(number2)
        _result:float = reajuste(number1, number2)
        print(f'O salário de {number2} terá um reajuste'
              f' de {number1} porcentos e passará a ser {_result:.2f}')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")