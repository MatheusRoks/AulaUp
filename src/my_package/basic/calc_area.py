from my_package.clear import clear
from my_package.verify_and_convert import convert_float, verify_float

"""
-----------------MODO BÁSICO--------------------
o usuario recebe um valor para o raio;
multiplica o valor do raio por ele mesmo;
multiplica o resultado pelo valor de pi (3.14);
o resultado é a área do círculo;

"""
PI_B = 3.14
raio = input("Informe o valor do raio: ")
print("Cálculo da área do círculo")
print(
    f"Para uma cirunferencia {raio} de raio, temos {PI_B * (float(raio) ** 2):.2f}"
    f" de área"
)

input("Pressione enter para continuar...")

"""
-------Modo simples---------
laço de repetição -> usuário insere os dados ->
verificação dos dados -> pi * r**2 -> valor
"""
while True:
    clear()
    print("cálculo da cricunferencia do círculo")
    r: str = input("Informe o valor do raio: ")
    PI = 3.1415

    if verify_float(r):
        _r: float = convert_float(r)[0]
        area: float = PI * (_r**2)
        print(f"Para uma cirunferencia {_r} de raio, temos {area:.2f} de área")
        break
    
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
