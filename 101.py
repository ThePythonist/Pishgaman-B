class Person :
    def __init__(self, name, age, height, weight, city, job):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.city = city
        self.job = job

    def Talk(self):
        print(f"""Hello my name is {self.name} and I am {self.age} years old
I am {self.height} centimeter and {self.weight} kilogram and
and I live in {self.city} and my job is {self.job}
""")

Mahan = Person("Mahan", 16, 179, 76, "New York","Game Developer")
Mahan.Talk()
