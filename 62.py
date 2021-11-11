x = 15
y = 25

def f(x,y):
    # numbers = list(range(x,y))
    # print(numbers)
    # x,y = 30,45
    numbers = range(x,y)
    print(*numbers)

# f(int(input("Enter x : ")),int(input("Enter y : ")))
f(x,y)
