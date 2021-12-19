class Car :
    def __init__(self, name, model ):
        self.name = name
        self.model = model

    def Break(self):
        print("Break!")

    def Tell_Info(self):
        print("Car Name :",self.name)
        print("Car Model :",self.model)


benz = Car("s500","2014")
benz.Tell_Info()

bmw = Car("x6","2017")
bmw.Tell_Info()
