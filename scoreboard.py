from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.hideturtle()
        self.updateScoreboard()
    
    def scored(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()
        

    def updateScoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER!", align="center", font=("Arial", 24, "normal"))
