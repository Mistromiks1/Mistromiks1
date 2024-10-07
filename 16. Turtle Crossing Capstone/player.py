from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """Creating the initial turtle."""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.player_update()

    def player_update(self):
        """Places turtle at the starting position."""
        self.goto(STARTING_POSITION)

    def movement (self):
        """Makes the turtle move by a certain distance."""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)



