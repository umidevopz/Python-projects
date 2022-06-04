import turtle
from turtle import *

wn = turtle.Screen()
wn.title('Pong game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) #This function is used to turn turtle animation on or off and set a delay for update drawings

# while True:
#     wn.update()


#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=7, stretch_len=1)
paddle_a.penup() #this stops drawing
paddle_a.goto(-350, 0)

# paddle b 

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=7, stretch_len=1)
paddle_b.penup() #this stops drawing
paddle_b.goto(350, 0)


# ball 


ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup() #this stops drawing
ball.goto(0, 0)


# moving paddles

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_a.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()