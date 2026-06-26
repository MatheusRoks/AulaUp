"""
-------------MODO BÁSICO--------------------
usuário insere um valor pra velocidade média, um valor pro tempo gasto
se divide a velocidade média pelo tempo gasto, divide dnv por 12 q é a constante
exibe o resultado o resultado

"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

KM_L: int = 12

vm_b: str = input("Digite a velocidade média(km/h): ")
tg_b: str = input("Digite o tempo gasto em HORAS: ")
resultado: float = (float(vm_b) / float(tg_b)) / KM_L

print(
    f"Para um carro com a velocidade média de {vm_b}, num percurso que dura"
    f" {tg_b} hora a quantidade de litros gastos foi de {resultado}"
)

input("Pressione enter para continuar...")


"""
-----------modo simples-----------
laço de repetição -> usuário insere os dados ->
verificação dos dados -> (tempo/vm)/12 -> valor

"""
while True:
    clear()
    print("Calculo de quantidade de litros gastos")

    vm: str = input("Digite a velocidade média(km/h): ")
    tg: str = input("Digite o tempo gasto em HORAS: ")

    if verify_float(vm, tg):
        nums = convert_float(vm, tg)
        gas: float = (nums[0] / nums[1]) / KM_L
        print(
            f"Para um carro com a velocidade média de {vm}, num percurso que dura"
            f" {tg} hora a quantidade de litros gastos foi de {gas}"
        )
        break

    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
