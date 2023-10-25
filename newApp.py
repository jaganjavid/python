import turtle

# Create a turtle screen object
paper = turtle.Screen()

# Create a turtle object
pen = turtle.Turtle()

# Square

# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)

# Traingle  expalin the 60
# pen.forward(100)
# pen.right(120)
# pen.forward(100)
# pen.right(120)
# pen.forward(100)

# Octagenn 8 sides

# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)
# pen.forward(100)
# pen.right(45)

# Explain loop using with octa

# Looping
# For, While

# for times in range(8): # 0 --> 7
#     print(times)
#     pen.forward(100)
#     pen.right(45)

# for times in range(360): 
#     print(times)
#     pen.forward(1)
#     pen.right(1)

# for times in range(4): 
#     # print(times)
#     pen.forward(100)
#     pen.right(90)

# times = 0

# while times in range(4):
#     pen.forward(100)
#     pen.right(90)
#     times = times + 1

# i = 0

# while i<5:
#     print(i)
#     i = i + 1

# name = input("Enter your name ")

# print("your name is " + name)

# sides = input("How many sides you want to draw")
# sides = int(sides)

# for times in range(sides): 
#     # print(times)
#     pen.forward(100)
#     pen.right(360/sides)

# while True:

#     sides = input("How many sides you want to draw")
#     sides = int(sides)

#     myColour = input("Enter a Colour")

#     pen.color(myColour)

#     for times in range(sides): 
#         # print(times)
#         pen.forward(100)
#         pen.right(360/sides)

# pen.color("red")

# for times in range(4): 
#     # print(times)
#     pen.forward(100)
#     pen.right(90)

# pen.color("red")
# pen.forward(100)
# pen.right(90)
# pen.color("blue")
# pen.forward(100)
# pen.right(90)
# pen.color("green")
# pen.forward(100)
# pen.right(90)
# pen.color("orange")
# pen.forward(100)
# pen.right(90)

# Conditional Statement

for times in range(4):
    if times == 0:
        pen.color("red")
    if times == 1:
        pen.color("blue")
    if times == 2:
        pen.color("green")
    if times == 3:
        pen.color("yellow")
                    
    pen.forward(100)
    pen.right(90)
    
# This will keep the window open until you click on it
paper.mainloop()


# print
# variable
# datatypes
# library --> modules
# turtle
# looping - for / while
# input