from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

#Code to adjust the screen's display
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Michael's Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


#loop to make the snake move
game_is_on = True
while game_is_on:

    #causes a pause so the movement of each segment is not noticeable
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision with Food
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.new_score()
        snake.grow_snake_grow()

    #collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #collision with tail
    for bit in snake.snakey_bits[1:]:
        if snake.head.distance(bit) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()