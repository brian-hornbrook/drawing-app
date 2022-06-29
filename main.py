import turtle as turtle
import random

print(
    "Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(250)
turtle.pendown()


def star():
    for st in range(0, 5):
        turtle.pencolor("blue")
        turtle.forward(100)
        turtle.right(144)
        turtle.isvisible()


def square():
    for sq in range(0, 4):
        turtle.pencolor("blue")
        turtle.forward(100)
        turtle.right(90)


def hexagon():
    for h in range(0, 6):
        turtle.pencolor("blue")
        turtle.forward(100)
        turtle.right(60)


selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")

try:
    int(selection)

    if selection == "1":
        print("Excellent choice! Go to the result tab to see your creation.")
        star()
    elif selection == "2":
        print("Excellent choice! Go to the result tab to see your creation.")
        square()
    elif selection == "3":
        print("Excellent choice! Go to the result tab to see your creation.")
        hexagon()
    else:
        print("must choose 1 - 3")

except:
    print("you must choose a number")
