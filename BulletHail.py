#Initialization
import pygame, sys, time
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((1360, 660))
pygame.display.set_caption("Bullet Hail")
clock = pygame.time.Clock()

#Images
Ground = pygame.image.load("Images/RoomFloor.png")
HorizontalHallway = pygame.image.load("Images/HorizontalPassage.png")
VerticalHallway = pygame.image.load("Images/VerticalPassage.png")
avatar = pygame.image.load("Images/Avatar.png")

#Bullet class
class Bullet:
    def __init__(self, curving, velocity, pos, map_pos):
        self.curving = curving
        self.velocity = velocity
        self.pos = pos
        self.map_pos = map_pos
#Map class
class Map:
    def __init__(self):
        #Setting up the rects for each room/hallway
        self.RectSet = [pygame.Rect(0, 0, 1360, 660)]#############01
        self.RectSet.append(pygame.Rect(540, 660, 272, 544))######02
        self.RectSet.append(pygame.Rect(1360, 194, 524, 272))#####03
        self.RectSet.append(pygame.Rect(0, 1184, 1360, 660))######04
        self.RectSet.append(pygame.Rect(1884, 0, 1360, 660))######05
        self.RectSet.append(pygame.Rect(1360, 1378, 524, 272))####06
        self.RectSet.append(pygame.Rect(-524, 1378, 524, 272))####07
        self.RectSet.append(pygame.Rect(544, -524, 272, 524))#####08
        self.RectSet.append(pygame.Rect(-524, 194, 524, 272))#####09
        self.RectSet.append(pygame.Rect(0, -1184, 1360, 660))#####10
        self.RectSet.append(pygame.Rect(1360, -990, 524, 272))####11
        self.RectSet.append(pygame.Rect(-524, -990, 524, 272))####12
        self.RectSet.append(pygame.Rect(-1884, 0, 1360, 660))#####13
        self.RectSet.append(pygame.Rect(-1884, 1184, 1360, 660))##14
        self.RectSet.append(pygame.Rect(-1884, -1184, 1360, 660))#15
        self.RectSet.append(pygame.Rect(1884, -1184, 1360, 660))##16
        self.RectSet.append(pygame.Rect(1884, 1184, 1360, 660))###17
        self.RectSet.append(pygame.Rect(-1360, -524, 272, 524))###18
        self.RectSet.append(pygame.Rect(-1360, 660, 272, 524))####19
        self.RectSet.append(pygame.Rect(2408, -524, 272, 524))####20
        self.RectSet.append(pygame.Rect(2408, 660, 272, 524))#####21
    #Debugging(run "python3 BulletHail.py -h" instead to enable)
    def show_hitboxes(self):
        for maprect in self.RectSet:
            pygame.draw.rect(canvas, (255, 0, 0), maprect, 1)

    #checks if the player is in the Map
    def subrect(self, rect):
        colliding = 0
        for maprect in self.RectSet:
            if maprect.colliderect(rect) and partialsubrect(maprect, rect):
                colliding += 1
                if colliding == 2:
                    return True
            if subrect(maprect, rect):
                return True
        return False

    #The background moves to create the illusion of the player moving
    def move_player(self, x, y):
        for maprect in self.RectSet:
            maprect.left -= x
            maprect.top -= y

    #Displays the Map
    def display(self):
        for maprect in self.RectSet:
            if maprect.width == 1360:
                canvas.blit(Ground, maprect)
            elif maprect.width == 524:
                canvas.blit(HorizontalHallway, maprect)
            elif maprect.width == 272:
                canvas.blit(VerticalHallway, maprect)

#More initialization
world = Map()
right = False
left = False
up = False
down = False
playerect = pygame.Rect(630, 230, 101, 174)

#Subrect helper function for the Map class
def subrect(rect, subrect):
    if subrect.left >= rect.left and subrect.right <= rect.right and subrect.top >= rect.top and subrect.bottom <= rect.bottom:
        return True
    return False

#Another helper function for the Map class
def partialsubrect(rect, subrect):
    if int(subrect.left >= rect.left) + int(subrect.right <= rect.right) + int(subrect.top >= rect.top) + int(subrect.bottom <= rect.bottom) >= 3:
        return True

#Mainloop
while True:
    #Display everything
    canvas.fill((45, 30, 90))
    world.display()
    canvas.blit(avatar, playerect)
    if "-h" in sys.argv or "--hitboxes" in sys.argv: # Display hitboxes
        pygame.draw.rect(canvas, (0, 255, 0), playerect, 1)
        world.show_hitboxes()
    #Eventloop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right = True
                left = False
            if event.key == K_LEFT:
                left = True
                right = False
            if event.key == K_UP:
                up = True
                down = False
            if event.key == K_DOWN:
                down = True
                up = False
        if event.type == KEYUP:
            if event.key == K_LEFT:
                left = False
            if event.key == K_RIGHT:
                right = False
            if event.key == K_DOWN:
                down = False
            if event.key == K_UP:
                up = False
    #Moving the player here
    if right:
        world.move_player(10, 0)
        if not world.subrect(playerect):# Is it in the map bounds?
            world.move_player(-10, 0) # Move back if not

    if left:
        world.move_player(-10, 0)
        if not world.subrect(playerect):
            world.move_player(10, 0)
   
    if up:
        world.move_player(0, -10)
        if not world.subrect(playerect):
            world.move_player(0, 10)
  
    if down:
        world.move_player(0, 10)
        if not world.subrect(playerect):
            world.move_player(0, -10)
    pygame.display.update()
    clock.tick(45)
