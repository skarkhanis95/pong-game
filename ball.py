from turtle import Turtle
import global_variables

SCREEN_WIDTH = global_variables.SCREEN_WIDTH
SCREEN_HEIGHT = global_variables.SCREEN_HEIGHT
TOP_BORDER = int((SCREEN_HEIGHT/2) - 20)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.initialSpeed = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *=- 1
        self.initialSpeed +=1
        self.speed(self.initialSpeed)
