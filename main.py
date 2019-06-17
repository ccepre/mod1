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
    needed_points = np.array([x.split(",") for x in parentheses]).astype(np.int)
    #print(needed_points)
    #print(needed_points.shape)
    return (needed_points)

if __name__ == "__main__" :
    print("ok")
    needed_points = parser()
    map = field.Field(needed_points)
    map.resize(500)
