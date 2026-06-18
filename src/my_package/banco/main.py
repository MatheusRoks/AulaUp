from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def falar(self):...

class Professor(Person):
    def __init__(self, name:str, fala:str):
        self.name = name
        self.fala = fala

    def falar(self):
        print(f'O {self.name} diz "{self.fala}"')

name = Professor("antonio","Bom dia")
name.falar()

