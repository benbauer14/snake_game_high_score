from turtle import Turtle
import random

class Food(Turtle):
    #inherit Turtle
    def __init__(self):
        #Initalize super class Turtle
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.goto(random.randint(-275, 275), random.randint(-275, 275))
    
    def eaten(self):
        self.goto(random.randint(-275, 275), random.randint(-275, 275))
        