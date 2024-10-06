from turtle import Turtle

#Set fonts for the display
FONT = ("Courier", 70, "normal")
WINNER_FONT = ("Courier", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Scoreboard attributes"""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 300)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.l_player = input("Left Player: What is your name? ").title()
        self.r_player = input("Right Player: What is your name? ").title()


    def update_scoreboard(self):
        """Prints the scoreboard"""
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        """Score changes when left player scores a point"""
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        """Score changes when left player scores a point"""
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def winner(self):
        """Prints the winner screen when the score limit is reached"""
        if self.r_score == 10:
            self.goto(0, 0)
            self.write(f"The winner is\n {self.r_player}.\nSCORE = {self.r_score}:{self.l_score}", align="center", font=WINNER_FONT)

        if self.l_score == 10:
            self.goto(0, 0)
            self.write(f"The winner is\n {self.l_player}.\nSCORE = {self.l_score}:{self.r_score}", align="center", font=WINNER_FONT)