# TODO: Fix paddle bugs.

from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#creates the screen design
screen = Screen()
screen.bgcolor("black")
screen.title("Michael's Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

#creates paddles, ball and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

#causes screen to wait for button presses and uses them to move paddles
screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

#Loop to allow game to run
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.movement()

    #Detect collision with wall top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Hit with paddle
    elif ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #right paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #left paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    #Ends game at a score of 10
    elif scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_on = False
        scoreboard.winner()







screen.exitonclick()