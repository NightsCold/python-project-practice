# 定义类描述时钟
from time import sleep


class Clock(object):
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second+=1
        if self.second == 60:
            self.second = 0
            self.minute+=1
            if self.minute == 60:
                self.minute = 0
                self.hour+=1
                if self.hour == 24:
                    self.hour = 0
    def show(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

def main():
    clock = Clock(12,57,59)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ =='__main__':
    main()

# 定义类描述点
from math import sqrt

class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def move_to(self,x,y):
        self.x=x
        self.x=y
    def move_by(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def distence_to(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

def main():
    point1=Point(3,4)
    point2=Point()
    print(point1)
    print(point2)
    point1.move_to(5,5)
    point2.move_by(1,7)
    print(point1.distence_to(point2))

if __name__=='__main__':
    main()
