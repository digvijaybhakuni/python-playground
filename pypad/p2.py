
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


tiger = Animal(type='tiger')
cat = Animal(type='cat')

print(tiger)
print(cat)
# Animal is singleton, both will print cat
