from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia: int = agencia
        self.conta: int = conta
        self.saldo: float = saldo

    @abstractmethod
    def sacar(self, valor: float) -> bool: ...

    @abstractmethod
    def pagar(self, valor: float) -> None: ...
    def depositar(self, valor: float) -> float | None:
        if valor <= 0:
            print(f"O valor não pode ser {valor}")
            return None
        self.saldo += valor
        return self.saldo

    def to_dict(self) -> dict[str, str | int | float]:
        return {
            "Tipo": self.__class__.__name__,
            "Agência": self.agencia,
            "Conta": self.conta,
            "Saldo": self.saldo,
        }

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f"agencia={self.agencia}, conta={self.conta}, \
           saldo={self.saldo}"
        return f"{class_name}({attrs})"


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> bool:
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            return True
        print("Valor informado supera o saldo")
        return False

    def pagar(self, valor: float) -> None:
        self.sacar(valor + 2)


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int, saldo: float = 0, limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        self.limite_definido = limite

    def sacar(self, valor: float) -> bool:
        new_saldo = self.saldo + self.limite
        valor_pos_sac = self.saldo - valor
        if valor > self.saldo and valor <= new_saldo:
            excedente: float = valor - self.saldo
            self.saldo = 0
            self.limite -= excedente
            return True
        if valor_pos_sac >= 0:
            self.saldo -= valor
            return True
        print("Valor informado supera o saldo")
        return False

    def pagar(self, valor: float) -> None:
        self.sacar(valor + 2)
        return

    def depositar(self, valor: float) -> float | None:
        super().depositar(valor)
        if self.limite < self.limite_definido:
            devido: float = self.limite_definido - self.limite
            valor -= devido
            if valor > 0:
                return self.saldo + valor
            print("Valor utilizado para cobrir o cheque especial")
        return None

    def to_dict(self) -> dict[str, int | str | float]:
        dict_conta = super().to_dict()
        dict_conta.update({"Limite": self.limite})
        return dict_conta

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attrs = f"agencia={self.agencia}, conta={self.conta}, \
            saldo={self.saldo}, limite={self.limite}"
        return f"{class_name}({attrs})"
