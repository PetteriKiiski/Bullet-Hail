#Initialization
import pygame, sys, time
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((1360, 660))
pygame.display.set_caption("Bullet Hail")
clock = pygame.time.Clock()

#Images
Ground = pygame.images.load("RoomFloor.png")

#Bullet class
class Bullet:
    def __init__(self, curving, velocity, pos, map_pos):
        self.curving = curving
        self.velocity = velocity
        self.pos = pos
        self.map_pos = map_pos
class Player:
    def __init__(self, curving):
        self.curving = curving
        self.velocity = velocity
        self.map_pos = map_pos
class Map:
    def __init__(self):
        self.RectSet = [pygame.Rect(0, 0, 1360, 660)]#############01
        self.RectSet.append(pygame.Rect(544, 660, 272, 524))######02
        self.RectSet.append(pygame.Rect(1360, 194, 272, 524))#####03
        self.RectSet.append(pygame.Rect(0, 1184, 1360, 660))######04
        self.RectSet.append(pygame.Rect(1884, 0, 1360, 660))######05
        self.RectSet.append(pygame.Rect(1360, 2368, 524, 272))####06
        self.RectSet.append(pygame.Rect(-524, 2368, 524, 272))####07
        self.RectSet.append(pygame.Rect(524, -524, 272, 524))#####08
        self.RectSet.append(pygame.Rect(-524, 524, 272, 524))#####09
        self.RectSet.append(pygame.Rect(0, -1184, 1360, 660))#####10
        self.RectSet.append(pygame.Rect(1360, -660, 524, 272))####11
        self.RectSet.append(pygame.Rect(-524, -660, 524, 272))####12
        self.RectSet.append(pygame.Rect(-1884, 0, 1360, 660))#####13
        self.RectSet.append(pygame.Rect(-1884, 1184, 1360, 660))##14
        self.RectSet.append(pygame.Rect(-1884, -1184, 1360, 660))#15
        self.RectSet.append(pygame.Rect(1884. -1184, 1360, 660))##16
        self.RectSet.append(pygame.Rect(1884, 1184, 1360, 660))###17
        self.RectSet.append(pygame.Rect(-1360, -524, 272, 524))###18
        self.RectSet.append(pygame.Rect(-1360, 660, 272, 524))####19
        self.RectSet.append(pygame.Rect(2408, -524, 272, 524))####20
        self.RectSet.append(pygame.Rect(2408, 660, 272, 524))#####21
    def collide(self, rect):
        for maprect in self.RectSet:
            if rect.colliderect(maprect):
                return True
        return False
    def move_player(self, x, y):
        for maprect in self.RectSet:
            maprect.x -= x
            maprect.y -= y
    def display(self):
        for maprect in self.RectSet:
            canvas.blit
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(45)
