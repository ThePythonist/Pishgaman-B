class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

l,w = int(input("length : ")),int(input("width : "))

newRectangle = Rectangle(l,w)
print("rectangle area :",newRectangle.rectangle_area())
