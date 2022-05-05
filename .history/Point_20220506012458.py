class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def fallsinrectangle(self,rectangle):
        if(rectangle.lowleft.x<self.x<rectangle.highright.x and rectangle.lowleft.x<self.y<rectangle.highright.y):
            return True
        else:
            return False

    def distance(self,point):
        return ((point.x-self.x)**2+(point.y-self.y)**2)**0.5


class Rectangle:

    def __init__(self,lowLeft,highRight):
        self.lowLeft = lowLeft
        self.highRight=highRight
    

rectanglex=Rectangle(Point(1,2),Point(4,4))
p1 = Point(3,3)

print(p1.fallsinrectangle(rectanglex))