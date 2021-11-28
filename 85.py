# lines = open("words.txt",).readlines()
# lst = []
#
# for line in lines :
#     lst.append(line[:-1])
#
# output = "".join(lst)
#
# new_file = open("1line.txt","w").write(output)
# print("done")

# new_file = open("1line.txt",).readlines()
# print(*new_file)

lines = open("words.txt",).read().replace("\n"," ")
lst = []

for line in lines :
    lst.append(line)

output = "".join(lst)

new_file = open("1line.txt","w").write(output)
print("done")
