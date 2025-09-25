# Problem-1.py
# Calculator using a class
class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.strip().lower()

    def calculate(self):
        if self.operation in ("add", "addition", "+"):
            return self.a + self.b
        if self.operation in ("subtract", "subtraction", "-"):
            return self.a - self.b
        if self.operation in ("multiply", "multiplication", "*", "x"):
            return self.a * self.b
        if self.operation in ("divide", "division", "/"):
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        return "Invalid operation"

def main():
    # Example interactive run; for automated tests you can call Calculator(...) directly
    a = input("Enter a: ").strip()
    b = input("Enter b: ").strip()
    op = input("Operation (add/subtract/multiply/divide): ").strip()
    calc = Calculator(a, b, op)
    print("Result:", calc.calculate())

if __name__ == "__main__":
    main()
