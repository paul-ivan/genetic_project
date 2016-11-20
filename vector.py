#!/usr/bin/env python

import math


def dist(p1, p2):
    return math.hypot(p2[1] - p1[1], p2[0] - p1[0])

class Vector:
    def __init__(self, p1, p2):
        self.x = p2[0] - p1[0]
        self.y = p2[1] - p1[1]
    def compare(self, v2):
        return Vector(self.x, self.y, v2.x, v2.y)
    def show(self):
        print (str(self.x) + ", " + str(self.y))
    def norme(self):
        pass;
    def angle(self, v2):
        a = (math.atan2(v2.y, v2.x) - math.atan2(self.y, self.x)) * 180 / math.pi
        if (a > 180):
            a -= 360
        if (a < -180):
            a += 360
        return a



'''
v = Vector([0, 0], [0, 0])

p = Vector([0, 0], [1, 0])

print (p.angle(v))


'''
    

