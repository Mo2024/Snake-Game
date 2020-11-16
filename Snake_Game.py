#Imports python libraries
import sys
import pygame
import random
import os
import time

pygame.init()

#assigns thingys to window adjustments
size = width, height = 750, 750
white = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

#The coordinates and size of the snake square thingy
x = 200 
y = 200
w  = 25
h = 25
ax = range(30,700)
ay = range(40,700)
aw = 15
ah = 15
vel = 10
vertical1 = 9000
vertical2 = 0 

score_value = 0 
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
testy = 10

def show_score(x, y):
    score = font.render("Score: "+ str(score_value), True, (255,0,0))
    screen.blit(score, (x, y))

def apple(x,y):
   pygame.draw.rect(screen, (255, 0, 0),  (arx, ary, aw, ah))

def divisible_random(a,b,n):
    if b-a < n:
      raise Exception('{} is too big'.format(n))
    result = random.randint(a, b)
    while result % n != 0:
      result = random.randint(a, b)
    return result

arx = divisible_random(30,700,10)
ary = divisible_random(40,700,10)

    

while 1:
    
    #Delays the movement so you can see snake thingy fps
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #gets the presses to move the snake
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x= x - vel

    if keys[pygame.K_RIGHT]:
        x= x + vel

    if keys[pygame.K_DOWN]:
        y = y + vel

    if keys[pygame.K_UP]:
        y = y - vel

    screen.fill(white)

    #The snake thingy and apple thingy
    apple(arx, ary)
    snake = pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h))

    if x == arx and y == ary:
        score_value += 1



    #Borders for the frame thingy 
    pygame.draw.line(screen, (0,0,0), (14, 10), (14, 800), 30)
    pygame.draw.line(screen, (0,0,0), (734, 10), (734, 800), 30) 
    pygame.draw.line(screen, (0,0,0), (9000, 734), (0 , 734), 30) 
    pygame.draw.line(screen, (0,0,0), (9000, 24), (0 , 24), 30) 
  
    if x < 30:
        x = 700
    
    if x > 700:
        x = 30
    
    if y > 700:
        y = 40
    
    if y < 40:
        y = 700

    show_score(textx, testy)
    

    print(arx,ary,x,y)

    pygame.display.update()  
pygame.quit