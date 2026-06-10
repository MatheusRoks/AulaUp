quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1
    continuar = input("Deseja continuar? (S/N): ")
    if continuar.upper() == "N":
        break
media = soma / quantidade

print(f"Quantidade de números: {quantidade}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media:.2f}")
"""recebe numeros enquanto o usuário desejar, por fim printa a soma desses numeros e 
a média"""
