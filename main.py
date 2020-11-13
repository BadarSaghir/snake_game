# from turtle import Turtle, Screen
# import time
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.tracer(0)
import time
from snake import Snake, screen_start, screen

screen_start()

snake = Snake()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while snake.game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
