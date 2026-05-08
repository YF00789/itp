import math
from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass
class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a+b
class Subtract(Operation):
    def execute(self, a: float, b: float) -> float:
        return a-b
class Multiply(Operation):
    def execute(self, a: float, b: float) -> float:
        return a*b
class Divide(Operation):
    def execute(self, a: float, b: float) -> float:
        if b==0:
            raise ValueError("Division by zero is not allowed.")
        return a/b
class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return math.pow(a, b)