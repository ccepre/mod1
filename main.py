#!/usr/bin/env python
# coding: utf-8

import pygame 
import numpy as np 
import sys
import re
import field

def parser():
    lines = sys.stdin.read()
    parentheses = re.findall('\((.*?)\)', lines)
    needed_points = np.array([x.split(",") for x in parentheses]).astype(np.float)
    #print(needed_points)
    #print(needed_points.shape)
    return (needed_points)

if __name__ == "__main__" :
    needed_points = parser()
    map = field.Field(needed_points)
    map.resize()
    map.place_needed_points()
    map.gen_all_points()
    print(map.map_dots)