class Squar:
    def __init__(self,lenght,breadth):
        self.length=lenght
        self.breadth=breadth
    def area (self):    
        return self.length* self.breadth
r1 = Squar (50,60)
print ("The area of rectangle is:",r1.area ())