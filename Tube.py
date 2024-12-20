import random

import pygame





class Tube:
    def __init__(self):
        self.x = 800
        self.y = 0
        self.y2 = 600
        self.width = 50
        self.length = random.randint(0,450)


    def display(self, screen):
        pygame.draw.rect(screen,(200,30,15),(self.x,self.y,self.width,self.length))


    def move(self):
        self.x -= 2
        if self.x <= -50:
            self.x += 800
            self.length = random.randint(100,450)






















































































