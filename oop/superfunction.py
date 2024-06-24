class rectangle():
    def __init__(self,lenght,width) :
        self.lenght = lenght
        self.width = width
class square(rectangle):
    def __init__(self,lenght,width):
        super().__init__(lenght,width)
    def area(self):
        return self.lenght*self.width
class cube(rectangle):
    def __init__(self, lenght, width,height):
        super().__init__(lenght, width)
        self.height = height
    def volume(self):
        return self.lenght*self.width*self.height
square = square(3,3)
cube = cube(3,3,3)
print(square.area())
print(cube.volume())