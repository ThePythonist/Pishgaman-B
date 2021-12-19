class Calculator :
    def __init__(
            self,
            n1=float(input("Enter number 1 : ")),
            op=input("Enter operator : "),
            n2=float(input("Enter number 2 : ")),
    ):
        self.number1 = n1
        self.number2 = n2
        self.operator = op

    def add(self):
        return self.number1 + self.number2

    def substract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2

calc = Calculator()

if calc.operator == "+":
    print(calc.add())
elif calc.operator == "-":
    print(calc.substract())
elif calc.operator == "*":
    print(calc.multiply())
elif calc.operator == "/":
    print(calc.divide())
else :
    print("Thats not a valid operator")
