from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        file = open("highscore.txt")
        self.highscore = file.read()
        self.goto(0, 250)
        self.hideturtle()
        self.updateScoreboard()
        file.close()
    
    def scored(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()
        

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if(self.score > int(self.highscore)):
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.updateScoreboard()
    
    def increase_score(self):
        self.score += 1
        self.updateScoreboard()