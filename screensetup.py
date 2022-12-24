from turtle import Turtle, Screen
import global_variables
SCREEN_WIDTH = global_variables.SCREEN_WIDTH
SCREEN_HEIGHT = global_variables.SCREEN_HEIGHT
Y_POS = int(SCREEN_HEIGHT/2)
LINEMAN_HEADING = 270
LINE_MAN_FWD_DIST = 10
LINE_MAN_LOOP = int(SCREEN_HEIGHT / (LINE_MAN_FWD_DIST * 2))
class ScreenSetup:
    def __init__(self):
        self.create_line()

    def create_line(self):
        lineman = Turtle()
        lineman.hideturtle()
        lineman.speed("fastest")
        lineman.color("white")
        lineman.penup()
        lineman.goto(x=0, y=Y_POS)
        lineman.setheading(270)
        for _ in range(LINE_MAN_LOOP):
            lineman.pendown()
            lineman.forward(LINE_MAN_FWD_DIST)
            lineman.penup()
            lineman.forward(LINE_MAN_FWD_DIST)
