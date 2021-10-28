info = {
    "name":"leo",
    "age":34,
    "city":"los angles",
}

key = input("Enter any key to search : ")

if key in info :
    print("Found :",info[key])
else :
    print("Not Found")
