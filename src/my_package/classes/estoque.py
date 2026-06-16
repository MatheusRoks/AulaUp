from typing import Any

class Estoque:
    def __init__(self)->None:       
        self.estoque:list[Any] = []
        self.MSG_VALUE = "Valor não pode ser utilizado"
        self.MSG_EMPTY = "Estoque vazio"
        self.MSG_HAS = "O estoque já utiliza esse dado"

    def _error_msg(self, msg:str)->None:
       print(msg)

    def _recive(self, tipo:str)->str:
        valor:str = input(f"Digite um valor para {tipo}: ")
        return valor
    
    def _convert_int(self, type:str)->int|None:
        item:str = self._recive(type)
        try:
            valor_m = int(item)
            return valor_m
        except(TypeError, ValueError):
            return
       
    def _verify_has(self,type:int, _object:str|int):
        for i in self.estoque:
            if i[type] == _object:
                self._error_msg(self.MSG_HAS)
                return True
            return False
       
    def _verify_input(self, value:int|str|None, index:int)->bool:
        if not value:
            self._error_msg(self.MSG_VALUE)
            return False
        if self._verify_has(index, value):
            return False
        return True
           
    def create(self)->None:
        _id = self._convert_int("Código")
        if not self._verify_input(_id, 0):
            return
        name: str = self._recive("Nome")
        if not self._verify_input(name, 1):
            return
        amount= self._convert_int("Quantidade")
        self.estoque.append([_id, name, amount])
        return

    def search(self, code:int|None)-> None:
        if not self.estoque:
            self._error_msg(self.MSG_EMPTY)
            return
        for i in self.estoque:
            if not code:
                print(i)
                return
            if i[0] == code:
                print(i)
                return i


    def read_all(self)->None:
        self.search(None)

    def read_unic(self)->None:
        cod2 = self._convert_int("Código")
        self.search(cod2)
    
    def update_qnt(self):
        cod = self._convert_int("Código")
        qnt = self._convert_int("Quantidade")
        lista = self.search(cod)
        if lista:
            lista[2] = qnt

    def remove_item(self):
        cod = self._convert_int("Código")
        lista = self.search(cod)
        if lista:
            del lista

if __name__ == "__main__":
    estoque = Estoque()
    while True:
        print(
            f"------------Controle de estoque------------\n"
            f"1 - Adicionar produto\n"
            f"2 - Exibir estoque\n"
            f"3 - Exibir item\n"
            f"4 - Reescrita de estoque\n"
            f"5 - Remoção de item\n"
            f"6 - Sair\n"
            )
        option:str = input("Digite uma opção: ")
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