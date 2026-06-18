from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia:int, conta:int, saldo:float=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor:float)->bool:...

    def depositar(self, valor:float)->float|None:
        if valor<=0:
            print(f"O valor não pode ser {valor}")
        self.saldo+=valor
        return self.saldo
    
    def to_dict(self)->dict[str, str|int|float]:
        return {
            'Tipo': self.__class__.__name__,
            'Agência': self.agencia,
            'Conta': self.conta,
            'Saldo': self.saldo,
        }
    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = f'agencia={self.agencia}, conta={self.conta}, \
           saldo={self.saldo}'
        return f'{class_name}({attrs})'
    

class ContaPoupanca(Conta):
    def sacar(self, valor:float)->bool:
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque>=0:
            self.saldo-=valor
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, agencia:int, conta:int, saldo:float = 0, limite:float =0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        self.limite_definido = limite

    def sacar(self, valor:float)->bool:
       new_saldo = self.saldo+self.limite
       valor_pos_sac = self.saldo - valor
       if valor>self.saldo and valor<=new_saldo:
           self.saldo = 0
           self.limite -= self.saldo-valor
           return True
       elif valor_pos_sac>=0:
           self.saldo-=valor
           return True
       else:
           return False
       
    def depositar(self, valor:float)->float|None:
        super().depositar(valor)
        if self.limite < self.limite_definido:
            devido:float = self.limite - self.limite_definido
            valor-=devido
            if valor>0:
                return self.saldo+valor
            else:
                print("Valor utilizado para cobrir o cheque especial")

       
    def to_dict(self) -> dict[str, int|str|float]:
        dict_conta = super().to_dict()
        dict_conta.update({'Limite': self.limite})
        return dict_conta

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = f'agencia={self.agencia}, conta={self.conta}, \
            saldo={self.saldo}, limite={self.limite}'
        return f'{class_name}({attrs})'