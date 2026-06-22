import conta
import person

"""# class Banco:
#     def __init__(
#             self,
#             agencias:list[int]|None=None,
#             clientes:list[person.Person]|None=None,
#             contas:list[int]|None=None,
#     )"""


if __name__ == "__main__":
    c1 = person.Client("Matheus", 24)
    cc1 = conta.ContaCorrente(123, 321, 320, 600)
    c1.conta = cc1
    c2 = person.Client("João", 19)
    cp1 = conta.ContaPoupanca(123, 322, 320)
    c2.conta = cp1
    print(c1)
    print(cc1)
    print(cp1)
    cc1.pagar(320)
    cp1.pagar(318)
    print(cc1)
    print(c2)
    print(cp1)
