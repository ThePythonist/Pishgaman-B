lines = open("words.txt").readlines()
lst = []

for line in lines :
    if len(line) == 6 :
        lst.append(line)

print(lst)