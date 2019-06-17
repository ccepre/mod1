import numpy as np 

class Field():
    def __init__(self, needed_points, size=100, power=2):
        self.size = size
        self.power = power
        self.needed_points = needed_points
        self.map_dots = None
        self.all_points = None
    
    #def compute_new_size(self) :
    def resize(self):
        size = self.size
        self.map_dots = np.empty([size, size], dtype=object)
        div = np.amax(self.needed_points) / size
        translation = np.amin(self.needed_points[:, 0]) / (div * 2)
        self.needed_points[:, 0] = np.around((self.needed_points[:, 0] * (1 / div)) - translation)
        translation = np.amin(self.needed_points[:, 1]) / (div * 2)
        self.needed_points[:, 1] = np.around((self.needed_points[:, 1] * (1 / div)) - translation)
        self.needed_points[:, 2] = (self.needed_points[:, 2] * (1 / div))
        print(self.needed_points)
    
    def place_needed_points(self) :
        self.all_points = np.array(self.needed_points, copy=True)
        self.all_points = np.c_[self.all_points, np.ones(self.needed_points.shape[0])]
        for point in self.all_points :
            self.map_dots[int(point[0]), int(point[1])] = point
    
    def gen_point(self, x, y, power):
        array = np.array([x, y, 0, 1], dtype=float)
        point = self.all_points[0]
        num = 0
        den = 0
        for point in self.all_points :
            dist = np.linalg.norm(array[:2] - point[:2])
            if (dist == 0):
                num = point[2]
                den = 1
                continue
            num += point[2] / dist ** power
            den += 1 / dist ** power
        array[2] = num / den
        return(array)

    def gen_all_points(self):
        for x, line in enumerate(self.map_dots):
            for y, point in enumerate(line):
                if (point is not None):
                    continue
                point = self.gen_point(x, y, self.power)
                self.map_dots[x][y] = point