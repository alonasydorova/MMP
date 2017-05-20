import pygame
import random
import math
from pygame.locals import *
from sys import exit

counterObjects = 0

def beautifulPosition(img):
    xCoord = random.randint(0,sc_w-img.get_width())
    yCoord = random.randint(0,sc_h-img.get_height())
    return (xCoord,yCoord)

def beautifulScale(img, proportion):
    return pygame.transform.scale(img, (math.floor(img.get_width()*proportion),math.floor(img.get_height()*proportion)))

def randProportion(img):
    return random.randint(img.get_height()//4,img.get_height()//2)/img.get_height()

def isOkay(position, width, height):
    xMin = position[0]
    xMax = position[0] + width
    yMin = position[1]
    yMax = position[1] + height
    global occupation
    for counter in range(counterObjects):
        print(xMin)
        print(occupation["x"][counter][0])
        print(xMax)
        print(occupation["x"][counter][1])
        if (xMin >= occupation["x"][counter][0]) and (xMin <= occupation["x"][counter][1]):
            print("falsex")
            return False
        if (xMax >= occupation["x"][counter][0]) and (xMax <= occupation["x"][counter][1]):
            print("falsex")
            return False
        if (yMin >= occupation["y"][counter][0]) and (yMin <= occupation["y"][counter][1]):
            print("falsey")
            return False
        if (yMax >= occupation["y"][counter][0]) and (yMax <= occupation["y"][counter][1]):
            print("falsey")
            return False
    return True
def findAvailableSpace(img):
    for i in range(15):
        position = beautifulPosition(img) #randomly chosen position for the element
        if isOkay(position, img.get_width(), img.get_height()): #checks if there isn't any collision with other objects
            return position
    return beautifulPosition(img)

def stick(img, proportion=2, position=(-1,-1), fish=False):
    if proportion==2:
        proportion = randProportion(img)
    scaledImg = beautifulScale(img, proportion)
    if position == (-1,-1):
        position = findAvailableSpace(scaledImg)
    occupation["x"].append((position[0], position[0] + scaledImg.get_width()))
    occupation["y"].append((position[1], position[1] + scaledImg.get_height()))
    global counterObjects
    counterObjects += 1
    background.blit(scaledImg,position)
    if (fish):
        global pucci
        pucci = scaledImg
    pygame.display.update()

# =========================================================
sc_w = 1024 # screen width
sc_h = 780 # screen height
# Create program display area
pygame.init()
screen = pygame.display.set_mode((sc_w,sc_h), 0, 32)
pygame.display.set_caption("Voyage")
background = pygame.Surface((sc_w, sc_h), pygame.SRCALPHA, screen)
background.fill((20,75,127))
screen.blit(background, (0,0))
pygame.display.update()

slides = []
slides.append(pygame.image.load('./palma.png').convert_alpha())
slides.append(pygame.image.load('./fish.png').convert_alpha())
occupation = {"x": [], "y": []}

for i in range(5):
    stick(slides[0])
fishPos = (sc_w/2 - slides[1].get_width()/2, sc_h/2 - slides[1].get_height()/2)
fishMove = 0
stick(slides[1], 0.15, fishPos, True)
print(occupation)
# Event loop, just for stopping
# hahahahahhaha!
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            newPos = (pygame.mouse.get_pos()[0]-pucci.get_width()/2, pygame.mouse.get_pos()[1]-pucci.get_height()/2)
            while ((fishPos[0] != newPos[0]) or (fishPos[1] != newPos[1])):
                if (fishPos[0] < newPos[0]):
                    if (fishPos[1] <  newPos[1]): fishPos = (fishPos[0] + 1, fishPos[1] + 1)
                    elif (fishPos[1] > newPos[1]): fishPos = (fishPos[0] + 1, fishPos[1] - 1)
                elif (fishPos[0] >  newPos[0]):
                    if (fishPos[1] <  newPos[1]): fishPos = (fishPos[0] - 1, fishPos[1] + 1)
                    elif (fishPos[1] > newPos[1]): fishPos = (fishPos[0] - 1, fishPos[1] - 1)
                screen.blit(pucci,(fishPos[0],fishPos[1]))
                pygame.draw.rect(background, (0,0,0), ((fishPos[0] + pucci.get_width()/2),(fishPos[1] + pucci.get_height()/2),5,5), 0)
                pygame.display.update()
                #screen.blit(background, (0,0))
            #screen.blit(pucci,fishPos)
            #pygame.display.update()     
