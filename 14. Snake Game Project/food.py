import random as R
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x = R.randint(-280, 280)
        rand_y = R.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = R.randint(-280, 280)
        rand_y = R.randint(-280, 280)
        self.goto(rand_x, rand_y)

