# lines = open("words.txt").readlines()
# output = ""
#
# for line in lines :
#     if len(line) == 6 :
#         output += line
#
# # print(output)
# open("5-letter.txt","w").write(output)
# print("done")

lines = open("words.txt").readlines()
output = []

for line in lines :
    if len(line) == 6 :
        output.append(line)

mystr = ""
mystr.join(output)

open("5-letter.txt","w").write(mystr)
print("done")