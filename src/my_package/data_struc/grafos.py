from anytree import Node, RenderTree  # type: ignore


def criar_rede() -> Node: # type: ignore
    ana: Node = Node("Ana")# type: ignore
    bia: Node = Node("Bia", parent=ana)# type: ignore
    _: Node = Node("Carlos", parent=ana)# type: ignore
    _: Node = Node("Davi", parent=bia)# type: ignore
    return ana# type: ignore


def listar_amigos(usuario: Node) -> list[str]:# type: ignore
    return [filho.name for filho in usuario.children]  # type: ignore


def mostrar_rede(raiz: Node) -> None:# type: ignore
    for pre, _, node in RenderTree(raiz):  # type: ignore
        print(f"{pre}{node.name}")  # type: ignore


def existe_caminho(raiz: Node, destino: str) -> bool:# type: ignore
    return any(node.name == destino for node in raiz.descendants)  # type: ignore


def sugerir_amigos(usuario: Node) -> set[str]:# type: ignore
    sugestoes: set[str] = set()

    for amigo in usuario.children:  # type: ignore
        for amigo_de_amigo in amigo.children:  # type: ignore
            if amigo_de_amigo != usuario:
                sugestoes.add(amigo_de_amigo.name)  # type: ignore

    return sugestoes


if __name__ == "__main__":
    rede: Node = criar_rede()# type: ignore

    print("=== REDE ===")
    mostrar_rede(rede)# type: ignore

    print("\nAmigos da Ana:", listar_amigos(rede))# type: ignore

    print("\nExiste caminho até Davi?", existe_caminho(rede, "Davi"))# type: ignore

    print("\nSugestões para Ana:", sugerir_amigos(rede))# type: ignore
