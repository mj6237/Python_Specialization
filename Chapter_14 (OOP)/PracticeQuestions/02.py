# Rectangle Class

class Rectangle :
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self) :
        return self.width * self.height
    
    def perimeter(self) :
        return 2 * (self.width + self.height)
    def display_info(self) :
        print("<-----Rectangle Information----->")
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print("<------------------------------->")

my_rectangle = Rectangle(5,8)
my_rectangle.display_info()
        

