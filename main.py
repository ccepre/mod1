#!/usr/bin/env python
# coding: utf-8

import pygame 
import numpy as np 
import sys
import re
import field
import viewer

np.set_printoptions(threshold=sys.maxsize)
def parser():
    lines = sys.stdin.read()
    parentheses = re.findall('\((.*?)\)', lines)
    needed_points = np.array([x.split(",") for x in parentheses]).astype(np.float)
    #print(needed_points)
    #print(needed_points.shape)
    return (needed_points)

if __name__ == "__main__" :
    needed_points = parser()
    map = field.Field(needed_points, 50)
    map.resize()
    map.place_needed_points()
    map.gen_all_points()
    map.transform_all()
   # print(map.map_proj)
    viewer = viewer.Viewer(1000, 1000, map)
    viewer.initialization()
    viewer.run()
