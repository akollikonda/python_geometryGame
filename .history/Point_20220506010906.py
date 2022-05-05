from cv2 import sqrt


class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def fallsinrectangle(self,lowleft,highright):
        if(lowleft[0]<self.x<highright[0] and lowleft[1]<self.y<highright[1]):
            return True
        else:
            return False

    def distance(self,next):
        return sqrt((next[0]-self.x)**2+(next[1]-self.y)**2)