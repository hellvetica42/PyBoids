import math
from math import sqrt

def normalize(vec):
    if vec[0] == 1 and vec[1] == 1:
        return vec
    l = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
    vec[0], vec[1] = vec[0]/l, vec[1]/l
    return vec

def getDistance(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    return sqrt(x*x + y*y)

def getVecLen(vec):
    return math.sqrt(vec[0]**2 + vec[1]**2)


def getLeftVector(vec):
    normalize(vec)
    angle = math.asin(vec[1])
    angle += math.pi/2
    angle = round(angle, 4)
    left = [math.cos(angle), math.sin(angle)]
    return left

def getRightVector(vec):
    normalize(vec)
    angle = math.asin(vec[1])
    angle -= math.pi/2
    angle = round(angle, 4)
    right = [math.cos(angle), math.sin(angle)]
    return right