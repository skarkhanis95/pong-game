from turtle import Turtle
import global_variables
SCREEN_WIDTH = global_variables.SCREEN_WIDTH
SCREEN_HEIGHT = global_variables.SCREEN_HEIGHT
PADDLE_SPEED = 10
MOV_DIST = 30
BORDER = int((SCREEN_HEIGHT/2)-50)

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if not self.ycor() > BORDER:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if not self.ycor() < -abs(BORDER) + 20 :
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

