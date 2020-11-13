from turtle import Turtle, Screen

screen = Screen()
MOVE_DIS = 10
# turt = Turtle()


def screen_start():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)


class Snake:

    def __init__(self):
        self.turtles = []
        self.x = 0
        self.y = 0
        self.game_is_on = True
        self.create_snake()

    def move(self):
        for s in range(len(self.turtles) - 1, 0, -1):
            self.x = self.turtles[s - 1].xcor()
            self.y = self.turtles[s - 1].ycor()
            self.turtles[s].goto(x=self.x, y=self.y)

        self.turtles[0].forward(MOVE_DIS)

    def create_snake(self):
        for index in range(0, 3):
            turtle = Turtle()
            self.turtles.append(turtle)
            self.turtles[index].color("white")
            self.turtles[index].shape("square")
            self.turtles[index].penup()
            self.turtles[index].setx(x=self.x)
            self.x = self.x - 20
        self.x = 0

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(-90)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)
