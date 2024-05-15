
from abc import ABC, abstractmethod
from typing import Any


class Animal():

    _instance = None
    def __new__(cls, type: str):
        if cls._instance is None:
            print('create new instance')
            cls._instance = super().__new__(cls)
        return cls._instance
        

    def __init__(self, type: str):
        print('init class')
        self.type = type

    def __str__(self) -> str:
        return f'Animal {self.type}'

    def getType(self):
        return self.type

    @staticmethod
    def print():
        print("this is static")

    @classmethod
    def myclass(cls):
        print(cls)

tiger = Animal(type='tiger')
cat = Animal(type='cat')

tiger.print()

Animal.print()
Animal.myclass()

print(type(Animal))
print(type(tiger))

print(tiger)
print(cat)
# Animal is singleton, both will print cat



class Employee(ABC):

    @abstractmethod
    def name(self) -> Any:
        pass

    @abstractmethod
    def title(self):
        pass


class Manager(Employee):


    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.data = kwargs

    def name(self) -> Any:
        return self.data['name']

    def title(self) -> Any:
        return self.data['title']
    
    def __repr__(self) -> str:
        return str(self.data)

amit = Manager(name="Amit", title="Mr.")

print(amit.title(), amit.name())

