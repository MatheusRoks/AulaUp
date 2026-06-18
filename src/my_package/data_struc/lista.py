class Lista:
    def __init__(self, data: list[int | float]) -> None:
        self.data = data

    def maior(self) -> int | float:
        a: int | float = 0
        for i in range(len(self.data)):
            if self.data[i - 1] > a:
                a = self.data[i - 1]
            else:
                continue
        return a

    def maior_simp(self) -> int | float:
        self.data.sort()
        return self.data[-1]

    def menor(self) -> int | float:
        a: int | float = self.data[0]
        for i in range(len(self.data)):
            if self.data[i - 1] < a:
                a = self.data[i - 1]
            else:
                continue
        return a

    def menor_simp(self) -> int | float:
        self.data.sort()
        return self.data[-1]

    def soma_num(self) -> int | float:
        resultado: int | float = 0
        for i in range(len(self.data)):
            resultado += self.data[i - 1]
        return resultado

    def med(self) -> int | float:
        a: int | float = self.soma_num()
        media: int | float = a / len(self.data)
        return media

    def limpa(self) -> list[int | float]:
        for i in range(len(self.data)):
            for j in range(len(self.data) - 1, i, -1):
                if self.data[i] == self.data[j]:
                    del self.data[j]
        return self.data

    def reverse_list(self) -> list[int | float]:
        new: list[int | float] = []
        for i in range(len(self.data), 0, -1):
            new.append(self.data[i - 1])
        return new

    def pdata(self) -> list[int | float]:
        return self.data


listas = Lista([1, 2, 300, 4, 5, 3, 5, 2, 1, 2, 1, 3, 6, -1, 200])
print(listas.pdata())
listas.limpa()
print(listas.pdata())
print(listas.reverse_list())
