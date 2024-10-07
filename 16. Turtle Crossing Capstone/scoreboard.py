from turtle import Turtle

FONT = ("Courier", 18, "normal")
FINAL_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Scoreboard attributes."""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Prints the scoreboard."""
        self.goto(-380, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def new_level(self):
        """Updates the level when turtle reaches the finish line."""
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def crushed(self):
        """Creates the message when the turtle is hit by a car/Game is over."""
        self.goto(0,0)
        self.write(f"CRUSHED!!\nMax level reached is: {self.level}", align="center", font=FINAL_FONT)