"""
Exercício 15 — Sistema de Votação 
Crie um algoritmo que receba: 
quantidade de votos do candidato A;  
quantidade de votos do candidato B;  
quantidade de votos do candidato C;  
quantidade de votos brancos;  
quantidade de votos nulos.  
O algoritmo deve apresentar: 
total de votos;  
porcentagem de votos de cada candidato;  
porcentagem de votos brancos;  
porcentagem de votos nulos;  
quantidade de votos válidos.
"""
from my_package.clear import clear
class Calc_vot:
    def __init__(self, vA:int, vB: int, vC: int, vBr:int, vN:int):
        self.vA = vA
        self.vB = vB
        self.vC = vC
        self.vBr = vBr
        self.vN = vN

    def sum_total(self):
        soma = self.vA + self.vB + self.vC + self.vBr + self.vN 
        return soma

    def porcent(self):
        total = self.sum_total()
        votosA = total*(self.vA/100)
        votosB = total*(self.vB/100)
        votosC = total*(self.vC/100)
        votosvBr = total*(self.vBr/100)
        votosvN = total*(self.vN/100)
        return [votosA, votosB, votosC, votosvBr, votosvN]
    
    def sum_valid(self):
        somaV = self.vA + self.vB + self.vC 
        return somaV


while True:
    clear()
    print("Informe os votos obtidos")
    votosA = input("Digite os votos do candidato A : ")
    votosB = input("Digite os votos do candidato B: ")
    votosC = input("Digite os votos do candidato C: ")          
    votosBr = input("Digite de votos brancos: ")          
    votosN = input("Digite devotos votos nulos: ")          
    try:
        votosA, votosB, votosC, votosBr, votosN = int(votosA), int(votosB), int(votosC), int(votosBr), int(votosN)
        _result = Calc_vot(votosA, votosB, votosC, votosBr, votosN)
        clear()
        print(f"A quantidade de votos é {_result.sum_total()}")
        porcent = _result.porcent()
        print(f'A quantidade de votos que o candidato A recebeu foi {porcent[0]:.2f}%\n'
              f'A quantidade de votos que o candidato B recebeu foi {porcent[1]:.2f}%\n'
              f'A quantidade de votos que o candidato C recebeu foi {porcent[2]:.2f}%\n'
              f'A quantidade de votos branco recebeu foi {porcent[3]:.2f}%\n'
              f'A quantidade de votos nulos foi {porcent[4]:.2f}%\n'              
              )
        sumV = _result.sum_valid()
        print(f'A quantidade de votos válidos são {sumV}')
        break
    except:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")