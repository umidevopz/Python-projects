import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('My game')

#colors

White = (255, 255, 255)
Green = (0, 255, 0)
Blue = (0, 0, 128)
Black = (0, 0, 0)
Red = (255, 0, 0)

# coordinates of object 

x = 250
y = 250 

radius = 20

#velocity

vel = 5

# Run until the user asks to quit

running = True

while running:
    
    screen.fill((0,0,0))
    
    pygame.draw.circle(screen, (255,255,255), (int(x), int(y)), radius)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # get the state of all keyboard buttons
    
    userInput = pygame.key.get_pressed()
    
    #some conditions
    if userInput[pygame.K_LEFT] and x > 20:
        x -= vel
    if userInput[pygame.K_RIGHT] and x < 480:
        x += vel
    if userInput[pygame.K_UP] and y > 20:
        y -= vel
    if userInput[pygame.K_DOWN] and y < 480:
        y += vel
    
    
    pygame.time.delay(10)
    
    pygame.display.update()