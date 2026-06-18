from dataclasses import dataclass, field
from typing import cast


@dataclass
class Aluno:
    matricula: int
    nome: str
    notas: list[float] = field(default_factory=lambda: cast("list[float]", []))

    def __post_init__(self) -> None:
        print(f"Aluno(a) {self.nome} criado(a)!")

    def to_dict(self) -> dict[int, dict[str, str | list[float]]]:
        aluno: dict[int, dict[str, str | list[float]]] = {
            self.matricula: {"Nome": self.nome, "Notas": self.notas}
        }
        return aluno
