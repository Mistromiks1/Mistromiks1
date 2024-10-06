from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """Paddle attributes"""
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        """Controls upward movement of the paddles"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """Controls downward movement of the paddles"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



