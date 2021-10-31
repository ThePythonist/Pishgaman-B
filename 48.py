nomarat = {
    "riazi1":15,
    "gosaste":19,
    "farsi":12,
    "static":8,
    "madar manteghi":10,
}

for k,v in nomarat.items():
    if v >= 10 :
        print(k,": Passed")
    else :
        print(k,": Failed")

# nomarat_lst = [ int(i) for i in nomarat.values()]
# moadel = sum(nomarat_lst) / len(nomarat_lst)

moadel = sum(nomarat.values()) / len(nomarat)
print("Moadel :",moadel)
