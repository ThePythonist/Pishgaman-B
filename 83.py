lines = open("words.txt","r").readlines()
ing_words = []

for line in lines :
    if line[-4:-1] == "ing" :
        ing_words.append(line)

print(ing_words)
