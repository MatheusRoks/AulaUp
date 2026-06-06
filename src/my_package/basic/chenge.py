'''
usuário atribui 2 valores -> valor 2 é salvo em uma 3 variável, atribui-se valor
1 a váriavel 2 e variavel 3 a variavel 2 -> imprime.

'''
print("Iremos realizar a troca dos valores das variáveis: ")
varA = input("Valor da primeira variável: ")
varB = input("Valor da segunda variável: ")
print("Antes da troca: ")
print(f'VarA = {varA}')
print(f'VarB = {varB}')
varC = varB
varB = varA
varA = varC
print("depois da troca: ")
print(f'VarA = {varA}')
print(f'VarB = {varB}')
