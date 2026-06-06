from clear import clear
import math

while True:
    clear()
    a = input("Digite o coeficiente A: ")
    b= input("Digite o coeficiente B: ")
    c= input("Digite o coeficiente C: ")
    try:
        a, b, c = int(a), int(b), int(c)
        form = (b**2)-(4*a*c)
        if form>=0:
            raiz = math.sqrt(form)
            print(f'A raiz de {form:.2f} é {raiz:.2f}')
        else:
            print(f'O valor {form:.2f} não é possivel extrair raíz')
        break
    except:
        a:str = input("Os dados informados são inválidos, pressione enter para continuar ou N para sair")
        if a.upper == "N":
            break