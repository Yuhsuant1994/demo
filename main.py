# main.py
import fire
from src.add import add
from src.minus import minus

class Calculator:
    def add(self, a: int, b: int) -> int:
        """Adds two numbers."""
        return add(a, b)
    
    def minus(self, a: int, b: int) -> int:
        """Subtracts two numbers."""
        return minus(a, b)

if __name__ == "__main__":
    fire.Fire(Calculator)
