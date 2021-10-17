# lst = list()
# n = int(input("Enter length : "))
# c = 0
#
# while c < n :
#     x = int(input("Enter any number : "))
#     lst.append(x)
#     c += 1
#
# print(lst)

lst = list()
n = int(input("Enter length : "))
for i in range(n):
    n = int(input("Enter any number : "))
    lst.append(n)
print(max(lst))
