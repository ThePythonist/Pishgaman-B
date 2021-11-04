string = 'python'

index = [ i for i in range(len(string)) ]
print(dict(zip(string,index)))

# d = {}
#
# for i in range(len(string)):
#     d.setdefault(string[i],i)
#
# print(d)
