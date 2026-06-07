"""
usuário atribui 2 valores -> valor 2 é salvo em uma 3 variável, atribui-se valor
1 a váriavel 2 e variavel 3 a variavel 2 -> imprime.

"""

print("Iremos realizar a troca dos valores das variáveis: ")
var_a: str = input("Valor da primeira variável: ")
var_b: str = input("Valor da segunda variável: ")
print("Antes da troca: ")
print(f"VarA = {var_a}")
print(f"VarB = {var_b}")
var_c: str = var_b
var_b: str = var_a
var_a: str = var_c
print("depois da troca: ")
print(f"VarA = {var_a}")
print(f"VarB = {var_b}")
