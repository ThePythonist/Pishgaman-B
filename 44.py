numbers = []

for i in range(3):
    entry = input("Entry : ")

    try :
        entry = float(entry)
        numbers.append(entry)

    except ValueError :
        pass

print(numbers)
