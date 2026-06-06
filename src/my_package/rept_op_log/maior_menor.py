
lista = []
while len(lista)<=10:
    y = input("Digite um inteiro:")
    if y.isdigit():
        y=int(y)
        lista.append(y)
    else:
        print(f"O valor {y} não é um número, facilita ai")
    
lista.sort()
print(lista)

print(f'{lista[0]} é o menor valor')
print(f'{lista[-1]} é o maior valor')