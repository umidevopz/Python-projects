import turtle
 
wn = turtle.Screen()
wn.title('My pong game')
wn.bgcolor('black')
wn.setup(width=8000, height=600)
wn.tracer(0)

while True:
    wn.update()