lines = open("words.txt").readlines()
rev = []

for line in lines[:100] :
    rev.append(line[::-1])

output = "".join(rev)
open('rev.txt','w').write(output)
print('done')

# lines = open("words.txt").readlines()[:100]
# print(lines[::-1])
