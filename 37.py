lst1 = [11,22,33,44,55,66,77]
lst2 = [33,43,55,11,88,120]
lst3 = []

for number in lst1 :
    if number in lst2 :
        lst3.append(number)

print(lst3)
