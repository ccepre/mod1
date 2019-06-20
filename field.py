import numpy as np 
import pygame
import math
import sys
np.set_printoptions(threshold=sys.maxsize)


class Field():
    def __init__(self, needed_points, size=100, power=2):
        self.size = size
        self.power = power
        self.needed_points = needed_points
        self.map_dots = np.zeros([size * size, 4], dtype=float)
        self.map_proj = None

        self.color = (250,250,250)

        self.center = (0,0)
        self.scale = 10
        self.xtrans = 0
        self.ytrans = 0
        self.ztrans = 0
        self.xradian = 0.610865238
        self.yradian = 0.785398 
        self.zradian = 0
        self.radius =2 

    #def compute_new_size(self) :
    def resize(self):
        size = self.size
        prop = np.amax(self.needed_points) / size

        margin = np.amin(self.needed_points[:, 0]) / (prop * 2)
        self.needed_points[:, 0] = np.around((self.needed_points[:, 0]\
                * (1 / prop)) - margin - self.size / 2)

        margin = np.amin(self.needed_points[:, 1]) / (prop * 2)
        self.needed_points[:, 1] = np.around((self.needed_points[:, 1]\
                * (1 / prop)) - margin - self.size / 2)

        self.needed_points[:, 2] = (self.needed_points[:, 2] * (1 / prop))
        print(self.needed_points)
        print("-------------------------\n\n")

    def place_needed_points(self) :
        self.needed_points = np.c_[self.needed_points,\
                np.ones(self.needed_points.shape[0])]
        for point in self.needed_points :
            col = int(point[0] + self.size / 2)
            row = int(point[1] + self.size / 2)
            self.map_dots[col + row * self.size] = point

    def gen_point(self, x, y, power):
        array = np.array([x, y, 0, 1], dtype=float)
        num, den  = 0, 0
        for point in self.needed_points :
            dist = np.linalg.norm(array[:2] - point[:2])
            if (dist == 0):
                num, den  = point[2], 1
                continue
            num += point[2] / dist ** power
            den += 1 / dist ** power
        array[2] = num / den
        return (array)

    def gen_all_points(self):
        for i, point in enumerate(self.map_dots):
            x = i % self.size - self.size / 2
            y = math.floor(i / self.size) - self.size / 2
            if point[3] == 1 :
                continue
            self.map_dots[i] = self.gen_point(x, y, self.power)


    # TRANSFORMATION FUNCTIONS
    def scale_mat(self, s=1) :
        mat = np.array([[ s, 0, 0, 0],
                        [ 0, s, 0, 0],
                        [ 0, 0, s, 0],
                        [ 0, 0, 0, 1]])
        return (mat)

    def translate_mat(self, dx=0, dy=0, dz=0) :
        mat = np.array([[ 1, 0, 0, 0],
                        [ 0, 1, 0, 0],
                        [ 0, 0, 1, 0],
                        [dx,dy,dz, 1]])
        return (mat)

    def xrotate_mat(self, radians=0) :
        c = np.cos(radians)
        s = np.sin(radians)
        mat = np.array([[ 1, 0, 0, 0],
                        [ 0, c,-s, 0],
                        [ 0, s, c, 0],
                        [ 0, 0, 0, 1]])
        return (mat)
    
    def yrotate_mat(self, radians=0) :
        c = np.cos(radians)
        s = np.sin(radians)
        mat = np.array([[ c, 0, s, 0],
                        [ 0, 1, 0, 0],
                        [-s, 0, c, 0],
                        [ 0, 0, 0, 1]])
        return (mat)

    def zrotate_mat(self, radians=0) :
        c = np.cos(radians)
        s = np.sin(radians)
        mat = np.array([[ c,-s, 0, 0],
                        [ s, c, 0, 0],
                        [ 0, 0, 1, 0],
                        [ 0, 0, 0, 1]])
        return (mat)

    def transform_all(self) :
        self.map_proj = np.array(self.map_dots, copy=True)
        self.map_proj = np.dot(self.map_proj, self.scale_mat(self.scale))
        self.map_proj = np.dot(self.map_proj, self.xrotate_mat(self.xradian))
        self.map_proj = np.dot(self.map_proj, self.yrotate_mat(self.yradian))
        self.map_proj = np.dot(self.map_proj, self.zrotate_mat(self.zradian))
        self.map_proj = np.dot(self.map_proj, self.translate_mat(self.xtrans,\
                self.ytrans, self.ztrans))

    # DISPLAY FUNCTIONS
    def display(self, screen) :
        for i, point in enumerate(self.map_proj) :
            col = i % self.size
            row = math.floor(i / self.size)
            if (col + 1 < self.size) :
                pygame.draw.line(screen, self.color, point[:2],\
                        self.map_proj[i + 1][:2])
            if (row + 1 < self.size) :
                pygame.draw.line(screen, self.color, point[:2],\
                        self.map_proj[i + self.size][:2])
