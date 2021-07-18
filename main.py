from scoreboard import Scoreboard
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(600, 600)

screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.update()

snake = Snake()
scoreboard = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while game_over == False:
    screen.update()
    time.sleep(0.05)
    snake.move()

    #Detect colision with food
    if(snake.segments[0].distance(food) < 15):
        food.eaten()
        snake.addSeg()
        scoreboard.scored()

    #detect tail collisions
    for segment in snake.segments:
        if(segment == snake.segments[0]):
            pass
        elif(snake.segments[0].distance(segment) < 5):
            game_over = True
            scoreboard.gameover()

screen.exitonclick()