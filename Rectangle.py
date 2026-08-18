class Rectangle:
    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
    def area (self):    
        return self.length* self.breadth
r1 = Rectangle (20,30)
print ("The area of rectangle is:",r1.area ())