import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Creates the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Michael's Turtle Crossing")
screen.tracer(0)

#Listens for button press, creates the player, cars and scoreboard
turts = Player()
screen.listen()
screen.onkeypress(key="Up", fun=turts.movement)
cars = CarManager()
scoreboard = Scoreboard()

#Loop to keep game running until something happens
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.new_car()
    cars.cars_driving()

    #Detects if the turtle reaches the other side
    if turts.ycor() >= 280:
        turts.player_update()
        scoreboard.new_level()
        cars.speed_up()

    #Detects collision between car and turtle and ends the game.
    for car in cars.vehicles:
        if turts.distance(car) <= 20:
            game_is_on = False
            # screen.clear()
            scoreboard.crushed()

screen.exitonclick()