from collections import deque


def fila_clientes() -> None:
    fila: deque[str] = deque()
    while True:
        cliente = input("Cliente entrou: ")
        fila.append(cliente)
        if input("Finalizar? (s/n): ").strip().lower() == "s":
            break
    while fila:
        print(f"Cliente {fila.popleft()} saindo")


def impressora() -> None:
    fila: deque[str] = deque()
    while True:
        doc = input("Documento para imprimir: ")
        fila.append(doc)
        if input("Finalizar impressão? (s/n): ").strip().lower() == "s":
            break
    print("\nImprimindo")
    while fila:
        print(f"Imprimindo: {fila.popleft()}")


def banco() -> None:
    fila: deque[tuple[int, str]] = deque()
    senha: int = 1
    while True:
        nome: str = input("Nome do cliente: ")
        fila.append((senha, nome))
        print(f"Senha gerada: {senha}")
        senha += 1
        if input("Finalizar senhas? (s/n): ").strip().lower() == "s":
            break
    print("\nAtendimento")
    while fila:
        num, nome = fila.popleft()
        print(f"Senha {num} - {nome} sendo atendido")
