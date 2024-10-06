import turtle as t
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        """Defines the list for the snake body, creates the snake, sets the head"""


        self.snakey_bits = []
        self.new_snake()
        self.head = self.snakey_bits[0]

    def new_snake(self):
        """Creates the new snake of 3 segments"""

        for num in range (0, 3):
            self.new_seg(num)

    def move(self):
        """Makes the segments move into the space of the segment ahead of it to make the snake move."""

        for seg in range(len(self.snakey_bits) - 1, 0, -1):
            next_x = self.snakey_bits[seg - 1].xcor()
            next_y = self.snakey_bits[seg - 1].ycor()
            self.snakey_bits[seg].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def grow_snake_grow(self):
        """Snake grows when food is eaten"""
        self.new_seg(self.snakey_bits[-1].position())

    def new_seg(self, position):
        """finds the position where to add the segment."""
        x = 0
        y = 0

        snakey = t.Turtle(shape="square")
        snakey.color("white")
        snakey.penup()
        snakey.setpos(x, y)
        x -= 20
        self.snakey_bits.append(snakey)


    def up(self):
        """Makes the snake turn up"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        """Makes the snake turn down"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        """Makes the snake turn left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        """Makes the snake turn right"""
        if self.head.heading() != 180:
            self.head.setheading(0)

