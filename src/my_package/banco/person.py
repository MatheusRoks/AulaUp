import conta


class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

    @property
    def name(self)->str:
        return self.__name
    @name.setter
    def name(self, name:str)->None:
        self.__name = name

    @property
    def age(self)->int:
        return self.__age
    @age.setter
    def age(self, age:int)->None:
        self.__age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'Nome = {self.name!r}, Idade = {self.age!r}'
        return f'{class_name}{attrs}'
    
class Client(Person):
    def __init__(self, name:str, age:int):
        super().__init__(name, age)
        self.conta: conta.Conta|None= None
