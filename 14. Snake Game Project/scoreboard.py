from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, 'normal')


class Scoreboard(Turtle):
    """Attributes of the scoreboard"""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setpos(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes the scoreboard"""
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        """Updates the score and scoreboard with the new score when food is eaten"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Writes Game over and the final score when a collision occurs"""
        self.setpos(0, 0)
        self.write(f"GAME OVER.\nFinal Score = {self.score}", align=ALIGNMENT, font=FONT)
