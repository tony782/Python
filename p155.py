class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length

    def change_size(self, w, l):
        self.width = w
        self.length = l

rectangle = Rectangle(10,20)
print("A面積:", rectangle.area())
rectangle.change_size(20,40)
print("B面積:", rectangle.area())