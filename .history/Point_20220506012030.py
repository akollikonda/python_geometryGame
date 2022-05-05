from cv2 import sqrt

from Rectangle import Recatangle


class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def fallsinrectangle(self,rectangle):
        if(rectangle.lowleft[0]<self.x<rectangle.highright[0] and rectangle.lowleft[1]<self.y<rectangle.highright[1]):
            return True
        else:
            return False

    def distance(self,point):
        return ((point.x-self.x)**2+(point.y-self.y)**2)**0.5


p = Point(0,0)
p1=Point(3,4)
print(p.distance(p1))