import turtle
import random

# Creating two turtles and variables
flash = turtle.Turtle()
sonic = turtle.Turtle()

winner_present = False
turtles = [flash, sonic]

for turt in turtles:
    turt.speed(0)
    turt.penup()
    turt.shape('turtle')



flash.pencolor('orange')
sonic.pencolor('blue')


# prints the winner's name stating they won
def printWinner(name):
    if name == 'sonic':
        sonic.penup()
        sonic.home()
        sonic.pencolor('black')
        sonic.write('Sonic wins!', font=('System', 16, 'normal'))
        sonic.pendown()
    else:
        flash.penup()
        flash.home()
        flash.pencolor('black')
        flash.write('Flash wins!', font=('System', 16, 'normal'))
        flash.pendown()


# makes a square with given length and turtle to perform
def make_square(turt_name):
    turt_name.ht()
    for i in range(4):
        turt_name.forward(15)
        turt_name.left(90)


# makes a goal board by using the make_square function
def make_goal(turt_name, x, y):
    turt_name.penup()
    turt_name.setposition(x, y)
    turt_name.pendown()
    
    for i in range(2):
        for j in range(47):
            if j % 2 == 0:
                turt_name.begin_fill()
                turt_name.fillcolor('white')
            else:
                turt_name.begin_fill()
                turt_name.fillcolor('black')
            make_square(turt_name)
            turt_name.forward(15)
            turt_name.end_fill()
        turt_name.right(90)
        turt_name.forward(1)
        turt_name.right(90)
    turt_name.st()

make_goal(sonic, -355, -270)
make_goal(flash, -355, 270)
sonic.right(45)
flash.right(135)

sonic.penup()
# moving to the top corners
sonic.setposition(-325, 325)
flash.setposition(325, 325)
sonic.pendown()
flash.pendown()


while not(winner_present):

    # turtles go forward a random distance
    for turt in turtles:
        turt.forward(random.randint(0, 45))


    # checking if someone reached the goal
    if flash.ycor() <= -325:
        winner_present = True
        printWinner('flash')

    elif sonic.ycor() <= -325:
        winner_present = True
        printWinner('sonic')


turtle.mainloop()
