from cmath import pi
from turtle import circle


class circle:
    def __init__(self , radius , color):
        self.radius = radius
        self.color= color
    
    def getRadius(self):
        return self.radius
    def setRadius(self , radius):
        self.radius= radius
    
    def getColor(self):
        return self.color
    def setColor(self , color):
        self.color= color
    
    def areaofcircle(self):
        return pi * self.radius *2
    
    def printcircle(self):
        print(f'Radius = {self.radius} \n AreaofCircle = {self.areaofcircle()} \n colorofCircle: {self.color}')

c = circle(10 , 'red')
c.printcircle()

print("-"*20) #SPACE

class cylinder(circle):
    def __init__(self, radius, color , height):
        super().__init__(radius, color)
        self.height = height
    
    def getheight(self):
        return self.height
    def setheight(self , height):
        self.height = height

    
    def volumeofCylinder(self):
        return pi * self.height * self.radius * 2
    
    def displaycylinder(self):
        print(f'Radius = {self.radius} \n Height = {self.height} \n  ColorOfCylinder = {self.color} \n Volume of Cylinder = {self.volumeofCylinder()}')

cy= cylinder(10 , 'green' , 5)
cy.displaycylinder()