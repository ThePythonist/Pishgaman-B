def check_word(word):
    return "Pangram" if len(word) == len(set(word)) else "Not Pangram"

print(check_word(input("Entry : ")))
