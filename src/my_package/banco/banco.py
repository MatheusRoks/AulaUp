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
    cc2 = conta.ContaCorrente(110, 320, 10, 200)
    c2.conta = cc2
    print(c1)
    print(cc1)
    print(c2)
    print(cc2)
    cc1.transferir(321, cc2)
    print(cc1)
    print(cc2)
