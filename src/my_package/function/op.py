from my_package.verify_and_convert import convert_float
import math

def recebe()->(list[str]):
    num1:str = input("Digite o primeiro número: ")
    num2:str= input("Digite o segundo número: ")
    lista:list[str] = [num1, num2]
    return lista

def soma()->(float|str):
    nums = recebe()
    resp = "Valores inválido conta não pode ser executada."       
    try:
        new_number:list[float]=convert_float(*nums)
        resultado = new_number[0] +new_number[1]
        return resultado
    except ValueError:
        return resp
        
def sub()->(float|str):
    nums = recebe()
    resp = "Valores inválido conta não pode ser executada."
    try:
        new_numbers:list[float] = convert_float(*nums)
        resultado:float = new_numbers[0] - new_numbers[1]
        return resultado
    except ValueError:
        print("Valores inválido conta não pode ser executada.")
        return resp

def mult()->(float|str):
    resp = "Valores inválido conta não pode ser executada."
    nums = recebe()
    try:
        new_numbers:list[float] = convert_float(*nums)
        resultado:float = new_numbers[0] * new_numbers[1]
        return resultado
    except ValueError:
        print("Valores inválido conta não pode ser executada.")
        return resp

def div()->(float|str):
    numeros = recebe()
    resp = "Valores inválido conta não pode ser executada."

    if numeros[1] =="0":
        print(resp)
    try:
        nums:list[float] = convert_float(*numeros)
        resultado:float = nums[0]//nums[1]
        return resultado
    except ValueError:
            return resp
    
def pot()->(float|str):
    nums = recebe()
    resp = "Valores inválido conta não pode ser executada."

    if nums[0] =="0":
        return 1
    elif nums[1] =="0":
         return 0
    try:
        numbers:list[float] = convert_float(*nums)
        resultado:float = numbers[0]**numbers[1]
        return resultado
    except ValueError:
            return resp
    
def raiz()->(str|float):
    num:str = input("Digite o número para extrair a raiz: ")
    resp = "Valores inválido conta não pode ser executada."
    try:
        num2:float= float(num)
        if num2<=0:
            return resp
        return math.sqrt(num2)
    except(ValueError, TypeError):
        return resp
    
def raizcub()->(str|float):
    num:str = input("Digite o número para extrair a raiz: ")
    resp = "Valores inválido conta não pode ser executada."
    try:
        num2:float= float(num)
        if num2<=0:
            return resp
        return math.cbrt(num2)
    except(ValueError, TypeError):
        return resp
    
def fatorial()->(int|str|None):
    num = input("Digite o número que deseja o fatorial: ")
    resp = "Valores inválido conta não pode ser executada."
    resultado = 1
    try:
        number:int = int(num)
        while number>=1:
            resultado = resultado*number
            number-=1
        return resultado
    except ValueError:
        return resp

def numprim()->(str):
    num = input("Digite um número: ")
    resp = "Valores inválido conta não pode ser executada."
    notp = "Não é primo"
    ep = "É primo"
    try:
        num2:int=int(num)
        if num2<1 or num2%4==0 and num2%2==0:
            return notp