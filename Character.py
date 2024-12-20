import pygame


class Character:
    def __init__(self):
        self.x = 350
        self.y = 200
        self.side = 50
        self.speed = 1
        self.speedy = 1


    def display(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.side, self.side))

    def move(self):
        self.y += self.speed
        self.speed += 1









        # self.x += self.speed
        # self.y += self.speedy
        # if self.x == 750:
        #     self.speed = -1
        # if self.x == 0:
        #     self.speed = +1
        # if self.y == 300:
        #     self.speedy = +1
        # if self.y ==600:
        #     self.speedy = -1
        # if self.x >= 0:
        #     self.x += 1
        # if self.x >= 750:
        #     self.x -= 700+





























