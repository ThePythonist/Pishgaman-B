def calculator(x,y,operator):

    def add():
        return x + y

    def subtract():
        return x - y

    def multiply():
        return x * y

    def divide():
        return x / y

    if operator == "+":
        print(add())
    elif operator == "-":
        print(subtract())
    elif operator == "*":
        print(multiply())
    elif operator == "/":
        print(divide())

calculator(
    float(input("Enter first number : ")),
    float(input("Enter second number : ")),
    input("Enter operator : ")
)
