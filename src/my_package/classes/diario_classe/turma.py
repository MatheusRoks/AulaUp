from my_package.classes.diario_classe.alunos import Aluno


class Turma:
    def __init__(self) -> None:
        self.lista_de_estudantes: dict[int, dict[str, str | list[float]]] = {}
        self.MSG_VALUE = "Valor não pode ser utilizado"
        self.MSG_HAS = "Matricula já cadastrada"
        self.MSG_DONTHAVE = "Matricula inexistente"

    def _error_msg(self, msg: str) -> None:
        print(msg)

    def _input_data(self, tipo: str) -> str:
        data: str = input(f"Digite um valor para {tipo}: ")
        return data

    def _verify_int(self, valor: str) -> bool:
        try:
            int(valor)
            return True
        except ValueError:
            return False

    def _convert_int(self, tipo: str) -> int:
        while True:
            item = self._input_data(tipo)
            try:
                return int(item)
            except ValueError:
                self._error_msg(self.MSG_VALUE)
    def _convert_float(self, tipo:str)->float:
        while True:
            item = self._input_data(tipo)
            try:
                return float(item)
            except ValueError:
                self._error_msg(self.MSG_VALUE)

    def _verify_matricula(self, matricula: int) -> bool:
        return bool(matricula in self.lista_de_estudantes)

    def matricular(self) -> None:
        matricula: int = self._convert_int("matricula")
        if self._verify_matricula(matricula):
            self._error_msg(self.MSG_HAS)
            return
        nome: str = self._input_data("nome")
        aluno = Aluno(matricula, nome)
        aluno_dict = aluno.to_dict()
        self.lista_de_estudantes.update(aluno_dict)

    def adc_notas(self) -> None:
        matricula: int = self._convert_int("matricula")
        if not self._verify_matricula(matricula):
            self._error_msg(self.MSG_DONTHAVE)
            return
        print("Para acabar de adicionar as notas, envie uma mensagem vazia")
        cont = True
        while cont:
            option:str|None = self._input_data("notas")
            if option is None:
                cont=False
                return
            data = 