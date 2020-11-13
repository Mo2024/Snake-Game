#Imports python libraries
import sys
import pygame

pygame.init()

#assigns thingys to window adjustments
size = width, height = 750, 750
white = 255, 255, 255
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

#The coordinates and size of the snake square thingy
x = 200
y = 200
w = 20
h = 20
vel = 10


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
    #The snake thingy
    pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h))
    pygame.display.update()  

pygame.quit

