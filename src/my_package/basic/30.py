from my_package.clear import clear
from my_package.verify_and_convert import convert_int, verify_int

"""
recebe valor -> verifica se é int -> converte para int -> multiplica pela
constante -> mostra resultado
"""
MINUTO: int = 60
SEGUNDO: int = 60
while True:
    clear()
    print("Convertendo hora:minuto:segundo em segundo")
    num: str = input("Informe o horário(00:00:00): ")
    hora, minuto, seg = num.split(":")
    if verify_int(hora, minuto, seg):
        nums = convert_int(hora, minuto, seg)
        converted = (nums[0] * MINUTO + nums[1]) * SEGUNDO + nums[2]
        print(f"Total em segundos é: {converted}")
        break
    else:
        print("Valor inválido, tente novamente.")
        input("Pressione Enter para continuar...")
