from screensetup import ScreenSetup
from turtle import Turtle,Screen
from paddle import Paddle
import global_variables
from ball import Ball
import time
from scoreboard import ScoreBoard

LIMIT = 10
#Create Screen
screen = Screen()
screen.setup(width=global_variables.SCREEN_WIDTH, height=global_variables.SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
center_line = ScreenSetup()


l_paddle = Paddle((-380, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
screen.listen()
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
l_score = ScoreBoard((-50, 260))
r_score = ScoreBoard((50, 260))

game_is_on = True
sleep = 0.1
while game_is_on:
    if l_score.currentscore == LIMIT:
        game_is_on = False
        r_score.game_over("right")
    elif r_score.currentscore == LIMIT:
        game_is_on = False
        l_score.game_over("left")
    else:
        time.sleep(sleep)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
        if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
            ball.bounce_from_paddle()
            if not sleep < 0.06:
                sleep -= 0.01
                print(sleep)
        if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
            ball.bounce_from_paddle()
            if not sleep < 0.06:
                sleep -= 0.01
                print(sleep)
        if ball.xcor() > 400:
            l_score.add_score()
            ball.goto(0,0)
            sleep = 0.1
            ball.bounce_from_paddle()
        if ball.xcor() < -400:
            r_score.add_score()
            ball.goto(0, 0)
            sleep = 0.1
            ball.bounce_from_paddle()

screen.exitonclick()