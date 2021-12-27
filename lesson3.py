from turtle import *
import math


class Shape:
    start = [0,0]
    def get_distance(self,figure_1,figure_2):
        return [round(figure_2[0]-figure_1[0]), round(figure_2[1]-figure_1[0])]

class Circle(Shape):
    radius = 15
    def get_center(self):
        penup()
        goto(pos()[0], pos()[1]+self.radius/2)
        return pos()
    def get_area(self):
        return  math.pi * (self.radius*2)
    def move(self, x, y):
        penup()
        goto(x, y-(self.radius/2))
        pendown()
        circle(self.radius/2)

class Square(Shape):
    radius=15
    def get_center(self):
        penup()
        goto(pos()[0]+self.radius/2, pos()[1]+self.radius/2)
        return pos()
    def get_vertex(self):
        return 4
    def get_area(self):
        return self.radius*2
    def move(self,x,y):
        penup()
        goto(x-(self.radius/2), y-(self.radius/2))
        pendown()
        for i in range(4):
            forward(self.radius)
            left(90)

class  Triangle(Shape):
    radius = 15
    def get_center(self):
        penup()
        goto(pos()[0]+self.radius/2, pos()[1]+self.radius/(2*math.sqrt(3)))
        return pos()
    def get_vertex(self):
        return 3
    def get_area(self): 
        p=(self.radius+self.radius+self.radius)/2
        s=math.sqrt(p*(p-self.radius)*(p-self.radius)*(p-self.radius))
        return s
    def move(self, x, y):
        penup()
        goto(x-(self.radius/2), y-(self.radius/(2*math.sqrt(3))))
        pendown()
        for i in range(3):
            forward(self.radius)
            left(120)


goto(0, 0)
forward(200)
goto(0, 0)
left(90)
forward(150)
goto(0, 0)
right(90)



Circle().move(25, 20)
a=Circle().get_center()
print(a)
print(Circle().get_area())

goto(0, 0)

Square().move(50, 20)
b=Square().get_center()
print(b)
print(Square().get_area())

goto(0, 0)

Triangle().move(75, 20)
c=Triangle().get_center()
print(c)
print(Triangle().get_area())

print(Shape().get_distance(a,b))
print(Shape().get_distance(b,c))
print(Shape().get_distance(a,c))

done()