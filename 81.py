lines = open("words.txt","r").readlines()
max_len = ""

# for line in lines :
#     if len(line) > len(max_len) :
#         max_len = line
#
# print(max_len)
# print(len(max_len))
#---------------------------------------------------------------

lengths = []

for line in lines :
    if len(line) > len(max_len) :
        lengths.append(len(line))

max_len = max(lengths)
result = [ line[0:-1] for line in lines if len(line) == max_len ]

print(result)
