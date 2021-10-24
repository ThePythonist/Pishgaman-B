numbers = []

for i in range(3):
    entry = input("Entry : ")

    try :
        entry = float(entry)
        entry_string = str(entry)

        if entry_string[-2:] == ".0" :
            numbers.append(int(entry))
        else :
            numbers.append(entry)

    except ValueError :
        pass

print(numbers)
