books: list[dict[str, str]] = []
catalog: dict[str, dict[str, str]] = {}
wait_list: list[str] = []
history: list[str] = []


def register(id_: str, title: str, autor: str) -> None:
    liber = {"id": id_, "title": title, "autor": autor}
    books.append(liber)
    catalog[id_] = liber
    history.append(f"Livro adicionado: {title}")
    print("Livro cadastrado com sucesso.")


def search(code: str) -> None:
    if code in catalog:
        liber = catalog[code]
        history.append(f"Busca realizada: {code}")
        print("Livro encontrado")
        print("Código =", liber["id"])
        print("Autor =", liber["autor"])
        print("Título =", liber["title"])
    else:
        print("Livro não encontrado")


def wait_list_s(code: str) -> None:
    if code in catalog:
        wait_list.append(code)
        history.append(f"Empréstimo solicitado: {code}")
        print("Livro adicionado à lista de empréstimos")
    else:
        print("Livro não existe")


def waid_list_p() -> None:
    if len(wait_list) > 0:
        code = wait_list.pop(0)
        liber = catalog[code]
        history.append(f"Empréstimo realizado do livro: {code}")
        print(f"Livro emprestado: {liber['title']}")
    else:
        print("Nenhum empréstimo pendente")


def show_hist() -> None:
    print("Histórico")
    for i in range(len(history) - 1, 0, -1):
        print(history[i - 1])
