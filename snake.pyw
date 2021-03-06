import os
import turtle
import time
import random
from tkinter import messagebox

size = 600
halfLeft = ((size / 2) - 20) * (-1) # -290
halfRight = (size / 2) - 20 # 290
overflow = size + (size / 2)
delay = 0.15
score = 0
highScore = 0
savedHighScore = 0
fileName = "highScore.txt"

if os.path.isfile(fileName):
    with open(fileName) as f:
        savedHighScore = int(f.readline())
        if savedHighScore > highScore:
            highScore = savedHighScore
else:
    f = open(fileName, "w")
    f.write(str(0))
    f.close()

window = turtle.Screen()
window.title("Snake")
window.bgcolor("LightGray")
window.setup(width = size, height = size)
window.tracer(0)

name = window.textinput("What is your name?", "")
if name == "":
    name = "Player"

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("ForestGreen")
head.penup()
head.goto(0, 0)
head.direction = "stop"

snack = turtle.Turtle()
snack.speed(0)
snack.shape("circle")
snack.color("red")
snack.penup()

x = random.randint(halfLeft, halfRight)
y = random.randint(halfLeft, halfRight)
snack.goto(x, y)

segments = []

data = turtle.Turtle()
data.speed(0)
data.shape("square")
data.color("white")
data.penup()
data.hideturtle()
data.goto(0, 260)
data.write("Score: {}   High Score: {}".format(score, highScore), align = "center", font = ("Courier", 20, "normal"))

def writeData():
    data.clear()
    data.write("Score: {}   High Score: {}".format(score, highScore), align = "center", font = ("Courier", 20, "normal"))

    if highScore > savedHighScore:
        f = open(fileName, "w")
        f.write(str(highScore))
        f.close()

def randomSnack():
    x = random.randint(halfLeft, halfRight)
    y = random.randint(halfLeft, halfRight)
    snack.goto(x, y)

def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

def goRight():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

window.listen()
window.onkeypress(goUp, "w")
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "s")
window.onkeypress(goDown, "Down")
window.onkeypress(goLeft, "a")
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "d")
window.onkeypress(goRight, "Right")

while True:
    window.update()

    # if  (head.xcor() < halfLeft) or (head.xcor() > halfRight) or (head.ycor() < halfRight) or (head.ycor() > halfLeft):
    if  head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

    if head.distance(snack) < 20:
        randomSnack()

        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("LimeGreen")
        newSegment.penup()
        segments.append(newSegment)

        score += 10

        if score > highScore:
            highScore = score

        writeData()

        delay -= 0.0025

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            # time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(overflow, overflow)

            messagebox.showerror("", "Game over!")

            if highScore > savedHighScore:
                messagebox.showinfo("Congratulation", "Dear " + name + ", you broke the previous record (" +
                                    str(savedHighScore) + ")!\nThe new record is " + str(highScore) + " points.")

            segments.clear()
            randomSnack()
            score = 0
            writeData()
            delay = 0.15
    time.sleep(delay)

window.mainloop()