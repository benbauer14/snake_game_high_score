from turtle import Turtle,Screen
STARTING_POSITIONS = [(0,0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10

class Snake:
    def __init__(self):
        self.segments = []
        self.createSnake()

    def createSnake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) -1 ,0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)
        if(self.segments[0].xcor() >= 290 ):
            self.segments[0].goto(-290, self.segments[0].ycor())
        elif(self.segments[0].xcor() <= -290):
            self.segments[0].goto(290, self.segments[0].ycor())
        if(self.segments[0].ycor() >= 290 ):
            self.segments[0].goto(self.segments[0].xcor(), -290)
        elif(self.segments[0].ycor() <= -290):
            self.segments[0].goto(self.segments[0].xcor(), 290)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def left(self):
        if(self.segments[0].heading() != 0):
            self.segments[0].setheading(180)
    def right(self):
        if(self.segments[0].heading() != 180):
            self.segments[0].setheading(0)
    def up(self):
        if(self.segments[0].heading() != 270):
            self.segments[0].setheading(90)
    def down(self):
        if(self.segments[0].heading() != 90):
            self.segments[0].setheading(270)
    def addSeg(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[len(self.segments) - 1].xcor(),self.segments[len(self.segments) - 1].ycor() )
        self.segments.append(new_segment)