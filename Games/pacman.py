
# from random import choice
# from turtle import *

# from freegames import floor, vector

# state = {'score': 0}
# path = Turtle(visible=False)
# writer = Turtle(visible=False)
# aim = vector(5, 0)
# pacman = vector(-40, -80)
# ghosts = [
#     [vector(-180, 160), vector(5, 0)],
#     [vector(-180, -160), vector(0, 5)],
#     [vector(100, 160), vector(0, -5)],
#     [vector(100, -160), vector(-5, 0)],
# ]
# # fmt: off
# tiles = [
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
#     0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
#     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
# ]
# # fmt: on


# def square(x, y):
#     """Draw square using path at (x, y)."""
#     path.up()
#     path.goto(x, y)
#     path.down()
#     path.begin_fill()

#     for count in range(4):
#         path.forward(20)
#         path.left(90)

#     path.end_fill()


# def offset(point):
#     """Return offset of point in tiles."""
#     x = (floor(point.x, 20) + 200) / 20
#     y = (180 - floor(point.y, 20)) / 20
#     index = int(x + y * 20)
#     return index


# def valid(point):
#     """Return True if point is valid in tiles."""
#     index = offset(point)

#     if tiles[index] == 0:
#         return False

#     index = offset(point + 19)

#     if tiles[index] == 0:
#         return False

#     return point.x % 20 == 0 or point.y % 20 == 0


# def world():
#     """Draw world using path."""
#     bgcolor('black')
#     path.color('blue')

#     for index in range(len(tiles)):
#         tile = tiles[index]

#         if tile > 0:
#             x = (index % 20) * 20 - 200
#             y = 180 - (index // 20) * 20
#             square(x, y)

#             if tile == 1:
#                 path.up()
#                 path.goto(x + 10, y + 10)
#                 path.dot(2, 'white')


# def move():
#     """Move pacman and all ghosts."""
#     writer.undo()
#     writer.write(state['score'])

#     clear()

#     if valid(pacman + aim):
#         pacman.move(aim)

#     index = offset(pacman)

#     if tiles[index] == 1:
#         tiles[index] = 2
#         state['score'] += 1
#         x = (index % 20) * 20 - 200
#         y = 180 - (index // 20) * 20
#         square(x, y)

#     up()
#     goto(pacman.x + 10, pacman.y + 10)
#     dot(20, 'yellow')

#     for point, course in ghosts:
#         if valid(point + course):
#             point.move(course)
#         else:
#             options = [
#                 vector(5, 0),
#                 vector(-5, 0),
#                 vector(0, 5),
#                 vector(0, -5),
#             ]
#             plan = choice(options)
#             course.x = plan.x
#             course.y = plan.y

#         up()
#         goto(point.x + 10, point.y + 10)
#         dot(20, 'red')

#     update()

#     for point, course in ghosts:
#         if abs(pacman - point) < 20:
#             return

#     ontimer(move, 100)


# def change(x, y):
#     """Change pacman aim if valid."""
#     if valid(pacman + vector(x, y)):
#         aim.x = x
#         aim.y = y


# setup(420, 420, 370, 0)
# hideturtle()
# tracer(False)
# writer.goto(160, 160)
# writer.color('white')
# writer.write(state['score'])
# listen()
# onkey(lambda: change(5, 0), 'Right')
# onkey(lambda: change(-5, 0), 'Left')
# onkey(lambda: change(0, 5), 'Up')
# onkey(lambda: change(0, -5), 'Down')
# world()
# move()
# done()

import pygame
import random
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
 
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([100,100])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
 
 
class Ellipse(pygame.sprite.Sprite):
    def __init__(self,x,y,color,width,height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the background color and set it to be transparent
        self.image = pygame.Surface(&#91;width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ellipse
        pygame.draw.ellipse(self.image,color,&#91;0,0,width,height])
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
 
        
class Slime(pygame.sprite.Sprite):
    def __init__(self,x,y,change_x,change_y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        # Set the direction of the slime
        self.change_x = change_x
        self.change_y = change_y
        # Load image
        self.image = pygame.image.load("slime.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
 
    def update(self,horizontal_blocks,vertical_blocks):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.right &lt; 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left &gt; SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.bottom &lt; 0:
            self.rect.top = SCREEN_HEIGHT
        elif self.rect.top &gt; SCREEN_HEIGHT:
            self.rect.bottom = 0
 
        if self.rect.topleft in self.get_intersection_position():
            direction = random.choice(("left","right","up","down"))
            if direction == "left" and self.change_x == 0:
                self.change_x = -2
                self.change_y = 0
            elif direction == "right" and self.change_x == 0:
                self.change_x = 2
                self.change_y = 0
            elif direction == "up" and self.change_y == 0:
                self.change_x = 0
                self.change_y = -2
            elif direction == "down" and self.change_y == 0:
                self.change_x = 0
                self.change_y = 2
                
 
    def get_intersection_position(self):
        items = &#91;]
        for i,row in enumerate(enviroment()):
            for j,item in enumerate(row):
                if item == 3:
                    items.append((j*32,i*32))
 
        return items
    
        
def enviroment():
    grid = ((0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0),
            (0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,2,0))
 
    return grid
 
def draw_enviroment(screen):
    for i,row in enumerate(enviroment()):
        for j,item in enumerate(row):
            if item == 1:
                pygame.draw.line(screen, BLUE , &#91;j*32, i*32], &#91;j*32+32,i*32], 3)
                pygame.draw.line(screen, BLUE , &#91;j*32, i*32+32], &#91;j*32+32,i*32+32], 3)
            elif item == 2:
                pygame.draw.line(screen, BLUE , &#91;j*32, i*32], &#91;j*32,i*32+32], 3)
                pygame.draw.line(screen, BLUE , &#91;j*32+32, i*32], &#91;j*32+32,i*32+32], 3)
 