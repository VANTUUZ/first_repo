import random
# a = 'hello world'
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[2:5])
# print(a[2:])
# print(a[:4])
# print(a[])
# print(a[])

#
# a='Abrakadabra'
# b=len(a)
# print(b)
#
# c='a' in a
# d='e' in a
# print(c,d)
# print('a'.isupper())
# print('A'.isupper())
#
# data=input()
# if data.isupper():
#     print('DATA IS UPPERCASE')
# else:
#     print('data is lowercase')
# print('DATA IS UPPERCASE')
# data = input()
# if data.isupper() == False:
#     print('WRITE BIG LETTERS YOU IDIOT')


# i = 0
# while i < 10 :
#     print(i)
#     i += 1

# while True :
# #     print("lol")
#
#
# action = input()
# players_score = 0
# casino_score = 0
#
# while action == 'more' and players_score <= 21 and casino_score <= 21 :
#     players_score += random.randint(3,11)
#     casino_score += random.randint(3,11)
#     print(players_score)
#     action = input()
#
#
# if players_score == casino_score :
#     print('draw')
# elif players_score > 22 and casino_score >22 :
#     print('no wins')
# if 22 > players_s


# import random
# from unittest.mock import right

#
# wards = input()
#
# for i in range (len(wards),-1,-1):
#     print(wards[: i])
#
# wards = input()
# ghost_string = " "
#
# for i in range(len(wards)):
#     ghost_string += wards[i] +  " "  * random.randint(1,5 )
# print(ghost_string)
# cordinats = [5,3]
# instrictions = ['left', 'right', 'left', 'up']
#
# for i in instrictions:
#     if i == "left" :
#         cordinats[0] -= 1
#     if i == 'dawn':
#         cordinats[1] -= 1
#     if i == 'right' :
#         cordinats[0] += 1
#     if i == 'up' :
#         cordinats[1] += 1
#
# print(cordinats)

import pygame

from Character import Character
from Tube import Tube


screen = pygame.display.set_mode((800, 600))
character = Character()
tube = Tube()
tube2 = []
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.speed = -10
    screen.fill((0,0,0))
    character.display(screen)
    character.move()
    tube.display(screen)
    tube.move()
    pygame.display.flip()
    clock.tick(70)