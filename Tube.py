import random

import pygame


class Tube:
    def __init__(self):
        self.x = 800
        self.y = 0
        self.x2 = 800
        self.y2 = 350
        self.width = 70
        self.width2 = 70
        self.length = random.randint(0, 250)
        self.length_2 = random.randint(350, 600)

    def display(self, screen):
        pygame.draw.rect(screen, (200, 30, 15), (self.x, self.y, self.width, self.length))
        pygame.draw.rect(screen, (200, 30, 15), (self.x2, self.y2, self.width2, self.length_2))

    def move(self):
        self.x -= 2
        self.x2 -= 2
        if self.x <= -50:
            self.x += 800
            self.length = random.randint(0, 250)
        if self.x2 <= -50:
            self.x2 += 800
            self.length_2 = random.randint(300, 600)
