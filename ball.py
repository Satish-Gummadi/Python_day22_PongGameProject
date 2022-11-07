from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.goto(0, 0)
        # self.speed(10)

    def move(self):
        self.forward(10)
        self.left(90)
        self.forward(10)
        self.right(90)