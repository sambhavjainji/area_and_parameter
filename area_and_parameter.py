#wap to create a class circle and find the area and parameter of the circle object of given radius

class circle():
    def __init__(self,r):
        self.r=r
        print(f"The area of circle is{self.area()}")
        print(f"The area of circle is{self.parameter()}")
    def area(self):
         a=3.14*pow((self.r),2)
         return a
    def parameter(self):
        a=2*3.14*(self.r)
        return a
