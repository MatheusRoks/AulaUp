from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
recebe valor -> verifica se é float -> converte para float -> executa: tempo/velocida
 -> mostra resultado
"""
while True:
    clear()
    print("Cálculo da distancia percorrida baseada no tempo e velocidade média")
    vm: str = input("Digite a velocidade média(km/h): ")
    tempo: str = input("Digite o tempo levado até concluir o percurso(em horas): ")
    if verify_float(vm, tempo):
        nums = convert_float(vm, tempo)
        distancia: float = nums[1] / nums[0]
        print(f"A distância percorrida foi {distancia}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
