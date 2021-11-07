# --------------- Required positional argument ---------------

def Taabe1(x):
    return x

print(Taabe1(15))

def Taabe2(a,b):
    print(a**b)

Taabe2(2,3)

def Taabe3(a):
    return a ** 2

print(Taabe3(int(input("Enter any number : "))))


# -------------------- Optional Argument --------------------

def f4(a=2):
    return a ** 3
print(f4(5))

def f5(a=2):
    return a
print(f5(14))

def f6(a=2, b=3):
    return a+b
print(f6(10,20))

def f7(a=int(input("Enter any number : "))):
    return a**2
print(f7(10))