numbers = []

for i in range(4):
    n = float(input("Enter any number : "))
    numbers.append(n)

numbers.sort()
# numbers.reverse()
numbers = numbers[::-1]
print(numbers)
