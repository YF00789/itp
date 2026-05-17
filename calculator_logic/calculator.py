import random
from .operations import Add, Subtract, Multiply, Divide, Power
from .utils import log_action
class Calculator:
    def __init__(self, storage_manager):
        self.storage = storage_manager
        self.__history = self.storage.load_state()
        self.operations = {
            '+': Add(),
            '-': Subtract(),
            '*': Multiply(),
            '/': Divide(),
            '^': Power()
        }
    @log_action
    def calculate(self, a: float, b: float, operator: str = "+") -> float:
        if operator not in self.operations:
            raise KeyError(f"Operator {operator} not supported.")
        result = self.operations[operator].execute(a, b)
        log_entry = {
            "id": random.randint(1000, 9999),
            "num1": a,
            "op": operator,
            "num2": b,
            "result": result
        }
        self.__history.append(log_entry)
        self.storage.save_state(self.__history)
        return result
    def get_history(self) -> list:
        return self.__history