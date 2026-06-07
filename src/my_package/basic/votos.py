"""
recebe os dados de votação -> valida os dados -> converte ->
chama a classe -> realiza as operações -> exibe os resultados
"""

from my_package.clear import clear
from my_package.verify_and_convert import convert_int, verify_int


class CalcVot:
    def __init__(self, va: int, vb: int, vc: int, vbr: int, vn: int) -> None:
        self.vA = va
        self.vB = vb
        self.vC = vc
        self.vBr = vbr
        self.vN = vn

    def sum_total(self) -> int:
        soma: int = self.vA + self.vB + self.vC + self.vBr + self.vN
        return soma

    def porcent(self) -> list[float]:
        total: int = self.sum_total()
        votos_a: float = total * (self.vA / 100)
        votos_b: float = total * (self.vB / 100)
        votos_c: float = total * (self.vC / 100)
        votos_vbr: float = total * (self.vBr / 100)
        votos_vn: float = total * (self.vN / 100)
        return [votos_a, votos_b, votos_c, votos_vbr, votos_vn]

    def sum_valid(self) -> int:
        soma_valid: int = self.vA + self.vB + self.vC
        return soma_valid


while True:
    clear()
    print("Informe os votos obtidos")
    votos_a = input("Digite os votos do candidato A : ")
    votos_b = input("Digite os votos do candidato B: ")
    votos_c = input("Digite os votos do candidato C: ")
    votos_vbr = input("Digite de votos brancos: ")
    votos_vn = input("Digite devotos votos nulos: ")
    if verify_int(votos_a, votos_b, votos_c, votos_vbr, votos_vn):
        nums: list[int] = convert_int(votos_a, votos_b, votos_c, votos_vbr, votos_vn)
        _result = CalcVot(nums[0], nums[1], nums[2], nums[3], nums[4])
        clear()
        print(f"A quantidade de votos é {_result.sum_total()}")
        porcent = _result.porcent()
        print(
            f"A quantidade de votos que o candidato A recebeu foi {porcent[0]:.2f}%\n"
            f"A quantidade de votos que o candidato B recebeu foi {porcent[1]:.2f}%\n"
            f"A quantidade de votos que o candidato C recebeu foi {porcent[2]:.2f}%\n"
            f"A quantidade de votos branco recebeu foi {porcent[3]:.2f}%\n"
            f"A quantidade de votos nulos foi {porcent[4]:.2f}%\n"
        )
        sum_valid = _result.sum_valid()
        print(f"A quantidade de votos válidos são {sum_valid}")
        break
    else:
        print("Os valores informados não são válidos")
        input("Pressione enter para nova tentativa")
