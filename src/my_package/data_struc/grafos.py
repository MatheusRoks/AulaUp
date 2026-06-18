from anytree import Node, RenderTree  # type: ignore


def criar_rede() -> Node:
    ana: Node = Node("Ana")
    bia: Node = Node("Bia", parent=ana)
    _: Node = Node("Carlos", parent=ana)
    _: Node = Node("Davi", parent=bia)
    return ana


def listar_amigos(usuario: Node) -> list[str]:
    return [filho.name for filho in usuario.children]  # type: ignore


def mostrar_rede(raiz: Node) -> None:
    for pre, _, node in RenderTree(raiz):  # type: ignore
        print(f"{pre}{node.name}")  # type: ignore


def existe_caminho(raiz: Node, destino: str) -> bool:
    return any(node.name == destino for node in raiz.descendants)  # type: ignore


def sugerir_amigos(usuario: Node) -> set[str]:
    sugestoes: set[str] = set()

    for amigo in usuario.children:  # type: ignore
        for amigo_de_amigo in amigo.children:  # type: ignore
            if amigo_de_amigo != usuario:
                sugestoes.add(amigo_de_amigo.name)  # type: ignore

    return sugestoes


if __name__ == "__main__":
    rede: Node = criar_rede()

    print("=== REDE ===")
    mostrar_rede(rede)

    print("\nAmigos da Ana:", listar_amigos(rede))

    print("\nExiste caminho até Davi?", existe_caminho(rede, "Davi"))

    print("\nSugestões para Ana:", sugerir_amigos(rede))
