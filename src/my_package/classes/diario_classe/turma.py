from my_package.classes.diario_classe.alunos import Aluno


class Turma:
    def __init__(self) -> None:
        self.lista_de_estudantes: dict[int, dict[str, str | list[float]]] = {}
        self.MSG_VALUE = "Valor não pode ser utilizado"
        self.MSG_HAS = "Matrícula já cadastrada"
        self.MSG_DONTHAVE = "Matrícula inexistente"

    def _error_msg(self, msg: str) -> None:
        print(msg)

    def _input_data(self, tipo: str) -> str:
        return input(f"Digite um valor para {tipo}: ")

    def _convert_int(self, tipo: str) -> int:
        while True:
            try:
                return int(self._input_data(tipo))
            except ValueError:
                self._error_msg(self.MSG_VALUE)

    def _verify_matricula(self, matricula: int) -> bool:
        return matricula in self.lista_de_estudantes

    def matricular(self) -> None:
        matricula = self._convert_int("matrícula")
        if self._verify_matricula(matricula):
            self._error_msg(self.MSG_HAS)
            return
        nome = self._input_data("nome")
        aluno = Aluno(matricula, nome)
        self.lista_de_estudantes.update(aluno.to_dict())
        print("Aluno matriculado com sucesso!")

    def lancar_nota(self) -> None:
        matricula = self._convert_int("matrícula")
        if not self._verify_matricula(matricula):
            self._error_msg(self.MSG_DONTHAVE)
            return
        notas = self.lista_de_estudantes[matricula]["notas"]
        if not isinstance(notas, list):
            return
        while True:
            entrada = self._input_data("nota (ENTER vazio para finalizar)")
            if entrada == "":
                break
            try:
                notas.append(float(entrada))
            except ValueError:
                self._error_msg(self.MSG_VALUE)

    def exibir_boletim(self) -> None:
        if not self.lista_de_estudantes:
            print("Nenhum aluno cadastrado.")
            return
        print("\n**** BOLETIM DA TURMA ****\n")
        for matricula, dados in self.lista_de_estudantes.items():
            nome = dados["nome"]
            notas = dados["notas"]
            if not isinstance(nome, str):
                continue
            if not isinstance(notas, list):
                continue
            media = sum(notas) / len(notas) if notas else 0.0
            status = "Aprovado" if media >= 7.0 else "Reprovado"
            print(
                f"Matrícula: {matricula} | Nome: {nome} | Média: {media:.2f} | {status}"
            )
