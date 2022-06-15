#Import and initialize the pygame library
import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

#Set up screen

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("My first pygame project")

screen.fill("black")

# Set up space here

space = pymunk.Space()
space.gravity = (0, 500)
#colors
 
White = (255, 255, 255)
Green = (0, 255, 0)
Blue = (0, 0, 128)
Black = (0, 0, 0)
Red = (255, 0, 0)

# object current co-ordinates 
x = 0
y = 0
  
# dimensions of the object 
width = 3
height = 3
  
# velocity / speed of movement
vel = 1

# Run until the user asks to quit

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, (255, 255, 255), (250, 250), 75)
    keys = pygame.key.get_pressed()

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<50-width:
          
        # increment in x co-ordinate
        x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    
    if keys[pygame.K_DOWN] and y<50-height:
    
        # increment in y co-ordinate
    
        y += vel
    
    # drawing object on screen which is rectangle here 
    
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    
    #Update the full display Surface to the screen
    
    pygame.display.flip()


pygame.quit()