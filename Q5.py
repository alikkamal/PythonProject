from cmath import pi
from copyreg import constructor

#NO.1
#default constructor

class default:
    def __init__(self):
        self.attri= 'default constructor'
    def displaydefault(self):
        print(self.attri)

object = default()
object.displaydefault()

print("-"*10)#SPACE



#parameterized constructor

class parameterized:
    def __init__(self, radius , color):
        self.radius = radius
        self.color = color
    
    def colorofcircle(self):
        return self.color

    def areaofcircle (self):
        return pi * self.radius * 2 
    def displaycircleinfo(self):
        print(f"Areaofradius = {self.areaofcircle()} \n Color = {self.colorofcircle()}")
object = parameterized(10 , 'blue')
object.displaycircleinfo()



print("-"*10)





#NO.2

#Class

class student:
    #this is a student class
    def __init__(self , name , age , id):
        self.name = name
        self.age = age 
        self.id= id
    def displaystudentinfo(self):
        print(f'Name: {self.name} \n Age: {self.age} \n ID: {self.id}')

#object
std= student('ali',21 , 191)
std.displaystudentinfo()
