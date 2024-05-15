""" 
Dunder Function or Magic Function
Read more: https://realpython.com/python-magic-methods/
"""


class Stack:

    def __init__(self, items) -> None:
        self.items = list(items)

    def __contains__(self, item):
        for current_item in self.items:
            if item == current_item:
                return True
        return False


    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

    def __reversed__(self):
        return type(self)(reversed(self.items))

    def __str__(self) -> str:
        return f'Stack({self.items})'

    def __iter__(self):
        return iter(self.items)


stack = Stack([1, 2, 3, 4])

print(stack[1])

print(stack[-1])

print(len(stack))

print(reversed(stack))

print("Loop and Print")
[print(x) for x in stack]

name = "Digivjay"

print(f"Print {name=}")

print(f'{3 in stack = }')
print(f"{9 in stack = }")

class Factorial:
    def __init__(self):
        self._cache = {0: 1, 1: 1}

    def __call__(self, number):
        if number not in self._cache:
            self._cache[number] = number * self(number - 1)
        return self._cache[number]

factorial_of = Factorial()

print(factorial_of(4))
print(factorial_of(5))
print(factorial_of(2))


class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration


fib10 = [fib_number for fib_number in FibonacciIterator()]
print(fib10)

fib20 = [fib_number for fib_number in FibonacciIterator(stop=20)]
print(fib20)
