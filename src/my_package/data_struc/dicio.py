MSG = "Valor inválido"


class Agenda:
    def __init__(self) -> None:
        self.agenda: dict[str, dict[str, str]] = {}

    def novo(self, id_: str, name: str, number: str) -> dict[str, dict[str, str]]:
        return {
            id_: {
                "Nome": name,
                "Número": number,
            }
        }

    def dont_have(self) -> None:
        print("Não encontrado")

    def implement(self, contact: dict[str, dict[str, str]]) -> None:
        self.agenda.update(contact)

    def search(self, id_: str) -> str | None:
        if id_ not in self.agenda:
            self.dont_have()
            return None
        
        return (
            f" Nome: {self.agenda[id_]['Nome']}\n Número: {self.agenda[id_]['Número']}"
        )

    def deleta(self, id_: str) -> None:
        if id_ not in self.agenda:
            self.dont_have()
            return
        
        self.agenda.pop(id_)


class Venda:
    def __init__(self) -> None:
        self.estoque: dict[int, dict[str, str | float | int]] = {}
        self.vendedores: dict[str, float] = {}

    def adiciona_p(
        self, 
        id_: int, 
        name: str, 
        price: float, 
        qnt: int
    ) -> dict[int, dict[str, str | float | int]]:
        return {id_: {"Nome": name, "Valor": price, "Quantidade": qnt}}

    def adiciona_v(self, name: str) -> None:
        self.vendedores[name] = 0.0

    def implement(self, produto: dict[int, dict[str, str | float | int]]) -> None:
        self.estoque.update(produto)

    def busca(self, id_: int) -> dict[str, str | float | int] | str:
        if id_ in self.estoque:
            return self.estoque[id_]
        return MSG

    def deleta(self, id_: int) -> None:
        if id_ not in self.estoque:
            print(MSG)
            return
        self.estoque.pop(id_)

    def vender(self, id_produto: int, vendedor: str, quantidade: int) -> None:
        if vendedor not in self.vendedores:
            print("Vendedor não encontrado")
            return
        
        if id_produto not in self.estoque:
            print("Produto não encontrado")
            return
        
        product = self.estoque[id_produto]
        price: float = float(product["Valor"])
        total = price * quantidade

        self.vendedores[vendedor] = self.vendedores.get(vendedor, 0) + total

        product["Quantidade"] = int(product["Quantidade"]) - quantidade

    def ranking(self) -> None:
        for vendedor, ganhos in self.vendedores.items():
            print(f"{vendedor}: R$ {ganhos:.2f}")


class Frequencia:
    def __init__(self, texto: str) -> None:
        self.texto = texto

    def contar(self) -> dict[str, dict[str, int]]:
        cont: dict[str, dict[str, int]] = {}
        text = self.texto.lower().split()
        for palavra in text:
            if palavra in cont:
                cont[palavra]["quantidade"] += 1
            else:
                cont[palavra] = {"quantidade": 1}

        order: dict[str, dict[str, int]] = dict(
            sorted(cont.items(), key=lambda item: item[1]["quantidade"], reverse=True)
        )
        return order
