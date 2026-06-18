class Pilha:
    def history(self, pages: list[str]) -> str | None:
        if not pages:
            return None
        return pages.pop()

    def parenteses(self, conta: str) -> bool:
        x: list[str] = []
        for i in conta:
            if i == "(":
                x.append(i)
            elif i == ")":
                if not x:
                    return False
                x.pop()
        return len(x) == 0

    def desfazer(self, alteracoes: list[str]) -> str | None:
        if not alteracoes:
            return None
        return alteracoes.pop()
