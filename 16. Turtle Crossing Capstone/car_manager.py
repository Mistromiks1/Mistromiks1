import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager(Turtle):
    def __init__(self):
        """Car attributes"""
        super().__init__()
        self.vehicles = []
        self.hideturtle()
        self.starting_move_distance = 5
        self.move_increment = 5

    def new_car(self):
        """Creates a new car at a random location"""
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))

            y_start = random.randint(-250, 250)
            new_car.goto(400, y_start)
            self.vehicles.append(new_car)

    def cars_driving(self):
        """Makes cars move a certain distance each refresh."""
        for car in range(len(self.vehicles)):
            self.vehicles[car].forward(self.starting_move_distance)

    def speed_up(self):
        """Speeds up car."""
        self.starting_move_distance += self.move_increment




