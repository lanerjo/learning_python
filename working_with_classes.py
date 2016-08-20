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
        
#let's Define a rectangle
rectangle=Shape(100,45)
#let's call the class we just made with the function inside the class of area on our rectangle
print(rectangle.area()),"rectangle area"

#now let's call the above function twice
long_rectangle = Shape(120,10)
fat_rectangle = Shape(130,120)
###Both long_rectangle and fat_rectangle have their own functions and variables contained inside them - they are totally independent of each other. There is no limit to the number of instances I could create.
print(long_rectangle.area())
print(fat_rectangle.area())

#let's play with our rectangle variable by calling scaleSize
rectangle.scaleSize(0.5)

print(rectangle.area()),"scale sized rectangle area"

#next on to inheritance
