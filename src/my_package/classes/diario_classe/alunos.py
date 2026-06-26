from dataclasses import dataclass, field


@dataclass
class Aluno:
    matricula: int
    nome: str
    notas: list[float] = field(default_factory=lambda: [])

    def calcular_media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def to_dict(self) -> dict[int, dict[str, str | list[float]]]:
        return {
            self.matricula: {
                "nome": self.nome,
                "notas": self.notas,
            }
        }
