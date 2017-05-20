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
    return random.randint(img.get_height()//3,img.get_height())/img.get_height()

def isOkay(position, width, height):
    xMin = position[0]
    xMax = position[0] + width
    yMin = position[1]
    yMax = position[1] + height
    for singleObject in range(counterObjects):
        

def findAvailableSpace(img):
    while True:
        position = beautifulPosition(img) #randomly chosen position for the element
        if not isOkay(position, img.get_width(), img.get_height()): #checks if there isn't any collision with other objects
            return position

def stick(img, proportion=2, position=(-1,-1)):
    if proportion==2:
        proportion = randProportion(img)
    scaledImg = beautifulScale(img, proportion)
    if position == (-1,-1):
        position = findAvailableSpace(scaledImg)
    occupation["x"].append((position[0], position[0] + scaledImg.get_width()))
    occupation["y"].append((position[1], position[1] + scaledImg.get_height()))
    global counterObjects
    counterObjects += 1
    screen.blit(scaledImg,position)
    pygame.display.update()

# =========================================================

background = pygame.Color(20,75,127,0) # background color
sc_w = 1024 # screen width
sc_h = 780 # screen height

pygame.init()

# Create program display area
screen = pygame.display.set_mode([sc_w,sc_h])
pygame.display.set_caption("Voyage")

# Set background color
screen.fill(background)
pygame.display.update()

slides = []
slides.append(pygame.image.load('./palma.png').convert_alpha())
slides.append(pygame.image.load('./fish.png').convert_alpha())
occupation = {"x": [], "y": []}

for i in range(5):
    stick(slides[0])
stick(slides[1], 0.25, (sc_w/2,sc_h/2))
print(occupation)
    
# Event loop, just for stopping
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()