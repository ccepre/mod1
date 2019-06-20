import numpy as np 
import pygame
import math

SCROLL_UP = 5
SCROLL_DOWN = 4
class Viewer() :
    def __init__(self, width, height, field) :
        self.width = width
        self.height = height
        self.screen = None
        self.repeat_delay = 400
        self.repeat_interval = 30
        self.bg_color = (0, 0, 0)
        self.title = 'Mod1'
        self.field = field 

    def initialization(self) :
        pygame.init()
        pygame.key.set_repeat(self.repeat_delay, self.repeat_interval)
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg_color)
        self.field.display(self.screen)

        pygame.display.flip()

    def run(self) :
        running = True
        while running:
            # Event gestion
            mouse_press = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            rel = pygame.mouse.get_rel()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == SCROLL_UP :
                        self.field.scale += 1
                    if event.button == SCROLL_DOWN :
                        self.field.scale -= 1
            if (mouse_press[0] == 1) :
                self.field.xtrans += rel[0]
                self.field.ytrans += rel[1]
            if (mouse_press[2] == 1) :
                self.field.yradian += rel[0]/300
#                self.field.yradian = self.field.yradian % (2*math.pi)
 #               print("mod : " + str(self.field.yradian % math.pi / 2))
  #              yrad = self.field.yradian % math.pi
                self.field.xradian -= rel[1]/300
#                self.field.zradian -= rel[1]/300 
                print(self.field.yradian)
                print(self.field.zradian)
            self.screen.fill(self.bg_color)
            self.field.transform_all()
            print(np.around(self.field.map_proj[0:50]))
            self.field.display(self.screen)
            pygame.display.flip()

