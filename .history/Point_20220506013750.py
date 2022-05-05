from random import randint
from turtle import distance


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
        self.lowleft = lowLeft
        self.highright=highRight

    def area(self):
        l= self.lowleft.distance(Point(self.lowleft.x,self.highRight.y))
        w= self.highright.distance(Point(self.lowleft.x,self.highRight.y))
        return l*w

    

randomRectangle = Rectangle(Point(randint(1,10),randint(19,30)),Point(randint(10,20),randint(29,50)))

#x = float(input("Enter X cordinate of point"))
#y = float(input("Enter Y cordinate of point"))

#print(Point(x,y).fallsinrectangle(randomRectangle))
print("Area of rectangle = ",randomRectangle.area())