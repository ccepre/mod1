import numpy as np 

class Field():
    def __init__(self, needed_points):
        self.needed_points = needed_points
        self.map_dots = None
    
    #def compute_new_size(self) :
    def resize(self, size):
        self.map_dots = np.empty([size, size])
        print(self.needed_points)
        div = np.amax(self.needed_points)
        print(div)



