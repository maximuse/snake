import turtle
import time
import random

delay = 0.1

window = turtle.Screen()
window.title("Snake")
window.bgcolor("lightgray")
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

snack = turtle.Turtle()
snack.speed(0)
snack.shape("square")
snack.color("red")
snack.penup()
snack.goto(0, 100)

def goUp():
    head.direction = "up"

def goDown():
    head.direction = "down"

def goLeft():
    head.direction = "left"

def goRight():
    head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    if head.direction == "down":
        head.sety(head.ycor() - 20)

    if head.direction == "left":
        head.setx(head.xcor() - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)

window.listen()
window.onkeypress(goUp, "w")
window.onkeypress(goDown, "s")
window.onkeypress(goLeft, "a")
window.onkeypress(goRight, "d")
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "Down")
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")

while True:
    window.update()

    if head.distance(snack) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snack.goto(x, y)


    move()
    time.sleep(delay)

window.mainloop()
