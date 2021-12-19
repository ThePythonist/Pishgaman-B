# Verasat
# class A :
#     def say_hello(self):
#         print("Hello")
#
# class B(A) :
#     def say_goodbye(self):
#         print("Goodbye")
#
# b = B()
# b.say_goodbye()
# b.say_hello()
#
# Super()
# class Pedar :
#     def __init__(self,fname):
#         self.familyname = fname
#
#     def say_hello(self):
#         print("Hello")
#
# class Farzand(Pedar):
#     def __init__(self,fname):
#         super().__init__(fname)
#
#     def say_goodbye(self):
#         print("Goodbye")
#
# pesar = Farzand("Ahmadi")
# print(pesar.familyname)
#
# Without inheritance
class A :
    def __init__(self, fname="Ahmadi"):
        self.familyname = fname

    def say_hello(self):
        print("Hello")

class B :
    def __init__(self):
        self.parent = A()

    def say_goodbye(self):
        print("Goodbye")

child = B()
print(child.parent.familyname)
