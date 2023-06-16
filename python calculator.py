import math

class ScientificCalculator:

    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y

    def root(self, x, y):
        return math.sqrt(x) ** y

    def factorial(self, x):
        return math.factorial(x)

    def pi(self):
        return math.pi

    def e(self):
        return math.e

    def memory_store(self, x):
        self.memory = x

    def memory_recall(self):
        return self.memory

def main():
    calculator = ScientificCalculator()
    print(calculator.add(1, 2))
    print(calculator.subtract(3, 2))
    print(calculator.multiply(4, 5))
    print(calculator.divide(6, 2))
    print(calculator.power(2, 3))
    print(calculator.root(9, 2))
    print(calculator.factorial(5))
    print(calculator.pi())
    print(calculator.e())
    calculator.memory_store(10)
    print(calculator.memory_recall())

if __name__ == "__main__":
    main()
