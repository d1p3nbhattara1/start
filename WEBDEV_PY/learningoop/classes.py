#learing to create classes in python 
#class is like a theme/template for an object
#__init__() function:
#   use this function to assign values to object properties or other operation that are neccessary to do when the object is begin created
class point():
    def __init__(self,x,y):      #defines what should happen   when a new point is define .. auto calls it every time making a new point.... argument self presents the object in the question/moment...x,y are the coords of the point
        self.x = x # var after = can be called anything
        self.y = y
#create a new point  
p=point(7,7) #self.x=7 and so for y
print(p.x)
print(p.y)