# lst = list()
#
# for i in range(5):
#     n = int(input("Enter any number : "))
#     lst.append(n)

# lst.sort()
# print(lst[-1])
# print(max(lst))

lst = []

for i in range(5):
    lst.append(int(input("Enter any number : ")))

mymax = lst[0]

for index in lst :
    if index > mymax :
        mymax = index
print(mymax)
