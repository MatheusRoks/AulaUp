from typing import Any


class Conjuntos:
    def em_comum(self, x: set[str], y: set[str]) -> set[str]:
        return x & y

    def itens_diferentes(self, buy: list[str]) -> int:
        return len(set(buy))

    def repetidos(self, dados: list[Any]) -> bool:
        return len(dados) != len(set(dados))
