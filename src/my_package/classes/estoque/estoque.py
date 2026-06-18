class Estoque:
    def __init__(self) -> None:
        self.estoque: list[list[int | str]] = []
        self.MSG_VALUE = "Valor não pode ser utilizado"
        self.MSG_EMPTY = "Estoque vazio"
        self.MSG_HAS = "O estoque já utiliza esse dado"
        self.MSG_DONTSEARCH = "Produto não encontrado"

    def _error_msg(self, msg: str) -> None:
        print(msg)

    def _recive(self, tipo: str) -> str:
        valor: str = input(f"Digite um valor para {tipo}: ")
        return valor

    def _convert_int(self, tipo: str) -> int:
        while True:
            item = self._recive(tipo)
            try:
                return int(item)
            except ValueError:
                self._error_msg(self.MSG_VALUE)

    def _verify_has(self, index: int, _object: str | int) -> bool:
        for i in self.estoque:
            if i[index] == _object:
                self._error_msg(self.MSG_HAS)
                return True
        return False

    def _verify_input(self, index: int, value: int | str) -> bool:
        return not self._verify_has(index, value)

    def create(self) -> None:
        _id: int = self._convert_int("Código")
        if not self._verify_input(0, _id):
            return
        name: str = self._recive("Nome").strip()
        if not name:
            self._error_msg(self.MSG_VALUE)
        if not self._verify_input(1, name):
            return
        amount = self._convert_int("Quantidade")
        self.estoque.append([_id, name, amount])
        return

    def _verify_estoque(self) -> bool:
        if not self.estoque:
            self._error_msg(self.MSG_EMPTY)
            return False
        return True

    def read_all(self) -> None:
        if not self._verify_estoque():
            return
        for i in self.estoque:
            print(i)

    def read_unic(self) -> list[int | str] | None:
        if not self._verify_estoque():
            return None
        cod2 = self._convert_int("Código")
        for i in self.estoque:
            if i[0] == cod2:
                print(i)
                return i
        self._error_msg(self.MSG_DONTSEARCH)
        return None

    def update_qnt(self) -> None:
        lista = self.read_unic()
        if lista:
            qnt = self._convert_int("Quantidade")
            lista[2] = qnt

    def remove_item(self) -> None:
        lista = self.read_unic()
        if lista:
            self.estoque.remove(lista)


if __name__ == "__main__":
    estoque = Estoque()
    while True:
        print(
            "------------Controle de estoque------------\n"
            "1 - Adicionar produto\n"
            "2 - Exibir estoque\n"
            "3 - Exibir item\n"
            "4 - Reescrita de estoque\n"
            "5 - Remoção de item\n"
            "6 - Sair\n"
        )
        option: str = input("Digite uma opção: ")
        match option:
            case "1":
                estoque.create()
            case "2":
                estoque.read_all()
            case "3":
                estoque.read_unic()
            case "4":
                estoque.update_qnt()
            case "5":
                estoque.remove_item()
            case "6":
                input("Saindo...")
                break
            case _:
                print("Inválido saindo do programa")
                break
