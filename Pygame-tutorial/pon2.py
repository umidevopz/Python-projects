import pygame, sys
from pygame import *

pygame.init()
clock = pygame.time.Clock()

screen_wid = 1080
screen_ht = 660

screen = pygame.display.set_mode((screen_wid, screen_ht))
pygame.display.set_caption('Pong game')

#ball
ball = pygame.Rect(screen_wid/2 - 15, screen_ht/2 -15, 30,30)
player = pygame.Rect(screen_wid -20, screen_ht/2 -70, 10, 140)
opponent = pygame.Rect(10, screen_ht/2 -70, 10, 140)

#colors
bg_color = pygame.Color('grey12')
light = (255, 255, 255)

#looping 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light, opponent)
    pygame.draw.rect(screen, light, ball)
    pygame.draw.rect(screen, light, player)
pygame.display.flip()
clock.tick(60)