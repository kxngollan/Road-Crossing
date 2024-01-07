from turtle import Turtle

POSITION = [0, -260]

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(POSITION)
        self.setheading(90)

    def move_up(self):
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        if self.ycor() <= -260:
            pass
        else:
            self.setheading(270)
            self.forward(20)

    def move_left(self):
        if self.xcor() <= -260:
            pass
        else:
            self.setheading(180)
            self.forward(20)

    def move_right(self):
        if self.xcor() >= 260:
            pass
        else:
            self.setheading(0)
            self.forward(20)

    def reset(self):
        self.goto(POSITION)