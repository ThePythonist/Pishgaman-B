def factorial(n):
    if n == 1 :
        return n
    else :
        return n * factorial(n-1)
    # return n if n == 1 else n * factorial(n-1)

print(factorial(int(input("Enter any number : "))))
