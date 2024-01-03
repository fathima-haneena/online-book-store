class rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return print("area of the rectangle",(self.length*self.width))
    def perimeter(self):
        return print("perimeter of the rectangle",(2*self.length+2*self.width))
    def is_square(self):
        if self.length==self.width:
         
         return print(True,"the rectangle is a square")
        else:
         
         return print(False,"the rectangle is  not a square")


ob=rectangle(3,3)
ob.area()
ob.perimeter()
ob.is_square()