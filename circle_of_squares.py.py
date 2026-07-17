import turtle

meks=turtle.Turtle()

def draw_square():
    meks.color("BLACK")
    for side in range (4):
     meks.forward(100)
     meks.right(90)

draw_square()
for square in range (80):
    meks.speed(0)
    draw_square()
    meks.forward(5)
    meks.left(5)