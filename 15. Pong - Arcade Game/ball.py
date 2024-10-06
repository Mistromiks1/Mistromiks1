from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """Ball attributes"""
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.x_movement = 10
        self.y_movement = 10
        self.move_speed = 0.1

    def movement(self):
        """Controls ball movement"""
        new_x_cor = self.xcor() + self.x_movement
        new_y_cor = self.ycor() + self.y_movement

        self.goto(new_x_cor, new_y_cor)

    def bounce_y(self):
        """Controls the bounce of the ball from the walls"""
        self.y_movement *= -1

    def bounce_x(self):
        """Controls the bounce of the ball from the paddles"""
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball if the ball is missed."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()




