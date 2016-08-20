
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y=y 
        self.description='there is no description yet'
        self.author='nobody has claimed to make this shape yet'
        
    def area(self):
        return self.x*self.y
    
    def perimeter(self):
        return 2*self.x +2*self.y
    
    def describe(self,text):
        self.description=text
        
    def authorName(self,text):
        self.author=text
        
    def scaleSize(self,scale):
        self.x=self.x * scale
        self.y=self.y*scale
#Define a second class that takes our Class Shape as an argument
class Square(Shape):
    def __init__(self,x):
        self.x=x 
        self.y=x
#this class inherits from square which inherits from shape
class DoubleSquare(Square):
    def __init(self,y):
        self.x = 2*y
        self.y=y
    def perimeter(self):
        return 2*self.x+3*self.y
#our box is 4x4
box =DoubleSquare(4)
#now we call the perimeter function from our DoubleSquare class on box
print(DoubleSquare.perimeter(box)),"this is double square on box"
