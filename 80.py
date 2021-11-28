lines = open("words.txt","r").readlines()
items = []

for line in lines :
    items.append(line[:-1])

print(items)
