from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 25, "bold")
class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.currentscore = -1
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")
        self.add_score()
    def add_score(self):
        self.clear()
        self.currentscore += 1
        diplay = str(self.currentscore)
        self.write(diplay, move=False,align=ALIGN,font=FONT)
    def game_over(self,position):
        if position == "left":
            x_cor = -150
        else:
            x_cor = 150
        self.clear()
        self.goto(x_cor, 0)
        self.write("GAME OVER",move=False, align=ALIGN, font=FONT)