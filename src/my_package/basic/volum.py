"""
laço de repetição -> usuário insere os dados ->
verificação dos dados -> pi * r**2 * altura -> valor
"""
from my_package.clear import clear
while True:
    clear()
    print("cálculo do volume do cilindro")
    r = input("Informe o valor do raio: ")
    h = input("Informe o valor da altura")
    PI = 3.1415
    try:
        r = float(r)
        h = float(h)
        vol = PI * (r**2)*h
        print(f'Para um cilindro com {r} de raio e {h} de altura, temos {vol:.2f} de volume')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")