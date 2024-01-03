class length():
    def getlength(self,length) :

        self.length=length
        return length
        
class breadth():
    def getbreadth(self,breadth):
        self.breadth=breadth
class area(length,breadth):
    def areas(self):
        print("the area is ",(self.length*self.breadth))
obj=area()
l=int(input("enter the length"))
b=int(input("enter the breadth"))
obj.getlength(l)
obj.getbreadth(b)
obj.areas()

