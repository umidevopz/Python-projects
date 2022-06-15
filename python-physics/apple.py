import pygame
import pymunk , sys

#creating objects

def create_apple(space):
    mass = (1,100)
    body = pymunk.Body(mass, body_type = pymunk.Body.DYNAMIC)
    body.position = (0,400)


pygame.init()
#set screen
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('apple physics')
clock = pygame.time.Clock()

#set space
space = pymunk.Space()
space.gravity = (0,500)


#loop here
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    space.step(1/50)
    pygame.display.update()
    clock.tick(120) #limiting frames per seconds
    
    