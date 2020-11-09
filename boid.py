import pygame
from bird import Bird
from utils import *
import numpy as np
import random

class Boid:


    def __init__(self, num, width, height, screen):
        self.surface = screen
        self.num_birds = num
        self.WIDTH = width
        self.HEIGHT = height
        self.birds = [Bird(random.randint(0,self.WIDTH), random.randint(0,self.HEIGHT)) for a in range(self.num_birds)]
        self.RANGE= 100
        pass

    def step(self, mul=1):
        for b in self.birds:
            b.step(mul)
            if b.pos_x > self.WIDTH:
                b.pos_x = 0
            elif b.pos_x < 0:
                b.pos_x = self.WIDTH

            if b.pos_y > self.HEIGHT:
                b.pos_y = 0
            elif b.pos_y < 0:
                b.pos_y = self.HEIGHT
        # self.step_separation()
        # self.step_alignment()
        self.optimised()

    def optimised(self):
        SEPARATION_C = 0.05
        ALIGNMENT_C = 0.05
        COHESION_C = 0.0001

        for b in self.birds:
            nearby = [br for br in self.birds if getDistance(b.getPos(), br.getPos()) < self.RANGE]

            #SEPARATION
            nearby_vectors = [[b.getPos()[0] - n.getPos()[0], b.getPos()[1] - n.getPos()[1]] for n in nearby]
            sum_len = sum([getVecLen(n) for n in nearby_vectors])

            if sum_len != 0:
                sum_x = sum([v[0] for v in nearby_vectors])
                sum_y = sum([v[1] for v in nearby_vectors])

                avg_vec = [sum_x/sum_len, sum_y/sum_len]
                normalize(avg_vec)
                # opposite_vec = [-avg_vec[0]*STRENGTH, -avg_vec[1]*STRENGTH]
                opposite_vec = [avg_vec[0]*SEPARATION_C, avg_vec[1]*SEPARATION_C]

                b.turnByVec(opposite_vec)

            #ALIGNMENT
            dir_vectors = [n.dir for n in nearby]
            avg_vec = sum(dir_vectors)/len(dir_vectors)
            b.turnByVec(avg_vec * ALIGNMENT_C)


            #COHESION
            # pos = [n.getPos() for n in nearby]
            # avgPos = [sum([x[0] for x in pos])/len(pos), sum([y[1] for y in pos])/len(pos)]
            avgPos = [self.WIDTH/2, self.HEIGHT/2]
            vec = [avgPos[0] - b.getPos()[0], avgPos[1] - b.getPos()[1]]
            b.turnByVec([vec[0] * COHESION_C, vec[1] * COHESION_C])


    def getBirds(self):
        return self.birds