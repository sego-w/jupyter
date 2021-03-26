# Class homework from the course
from math import sqrt
from math import pi
class Coor:
    def __init__(self,coord1Arg,coord2Arg):
        self.coord1 = coord1Arg
        self.coord2 = coord2Arg
        # print(f"The two coordinates are {self.coord1} and {self.coord2}")
    def dist(self):
        distance = sqrt((self.coord2[0]-self.coord1[0])**2 + (self.coord2[1]-self.coord1[1]**2))
        # print("The distance between the two coordinates is " + str(distance))
        return distance
    def slope(self):
        slop = (self.coord2[1] - self.coord1[1])/(self.coord2[0]-self.coord1[0])
        # print("The slope between the two coordinates has a magnitude of " + str(slop))
        return slop
testz = Coor((1,3),(5,9))
print("The distance between the two coordinates is " + str(testz.dist()) + " and the slope is " + str(testz.slope()) )

class Cylinder:
    def __init__(self,radarg,heightarg):
        self.radius = radarg
        self.height = heightarg
    def volume(self):
        vol = pi * (self.radius ** 2) * self.height
        return vol
testx = Cylinder(5,10)
print(f"The volume of the given cylinder is {testx.volume()}")








"""
Some weird stuff done while my dad tried to explain class logic to me
test_slope = testz.slope()
vasakpunkt = Coor((1,3),(5,9))
parempunkt = Coor((21,33),(45,59))
"""