import math
from utils import *
import numpy as np
import random

from numpy.core.numeric import normalize_axis_tuple
class Bird:


    def __init__(self, x, y):
        self.pos_x, self.pos_y = x, y 
        self.angle = random.random() * math.pi * 2
        self.dir = np.array([math.cos(self.angle), math.sin(self.angle)])
        pass

    def step(self, mul=1):
        self.pos_x += self.dir[0] * mul
        self.pos_y += self.dir[1] * mul

    def turn(self, angle):
        angle = math.radians(angle)
        normalize(self.dir)
        self.angle += angle

        if self.angle < 0:
            self.angle = self.angle + math.pi * 2
        if self.angle > math.pi * 2:
            self.angle = self.angle - math.pi * 2

        self.dir[0], self.dir[1] = math.cos(self.angle), math.sin(self.angle)
        normalize(self.dir)

    def turnByVec(self, vec):
        self.dir[0] += vec[0]
        self.dir[1] += vec[1]
        normalize(self.dir)
        self.angle = math.asin(self.dir[1])


    def getPos(self):
        return [self.pos_x, self.pos_y]

    def getPixelPos(self):
        return [math.floor(self.pos_x), math.floor(self.pos_y)]