import turtle
UP_ARROW='Up'
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
SPACEBAR="space"


UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP
def up():
    global direction
    direction=UP
    print('up up up in the sky')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y= old_pos[1]
    turtle.goto(x,y+10)
    print(turtle.pos())
def left():
    global direction
    direction=LEFT
    print('you LEFT (haha i am funny)')
    turtle.pos()
    x=old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x-10,y)
    print(turtle.pos())
def down():
    global direction
    direction=DOWN
    print('you are going down buddy')
    turtle.pos()
    old_pos=turtle.pos()
    x=old_pos[0]
    y= old_pos[1]
    turtle.goto(x,y-10)
    print(turtle.pos())

def right():
    global direction
    direction=RIGHT
    print("you made the right choice!")
    turtle.pos()
    x=old_pos=turtle.pos()
    x=old_pos[0]
    y=old_pos[1]
    turtle.goto(x+10,y)
    print(turtle.pos())
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)

turtle.listen()
