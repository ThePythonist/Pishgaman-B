import random

def generate():
    numbers = range(0,9)
    password = ""
    for i in range(5):
        password += str(random.choice(numbers))
    return password

generated_password = generate()
print(generated_password)
