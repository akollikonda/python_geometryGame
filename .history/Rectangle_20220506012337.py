from Point import Point


class Rectangle:

    def __init__(self,lowLeft,highRight):
        self.lowLeft = lowLeft
        self.highRight=highRight
    

rectanglex=Recatangle(Point(1,2),Point(4,4))
p1 = Point(3,3)

print(p1.fallsinrectangle(rectanglex))