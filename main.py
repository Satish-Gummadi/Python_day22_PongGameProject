# Creating a pong game

# Steps to create a pong game:
# 1) Create a screen
# 2) Create and move paddle
# 3) Create another paddle for another player
# 4) Create a ball and move it
# 5) Detect collision with wall and bounce it
# 6) Detect collision with paddle
# 7) Detect when paddle misses
# 8) Keep score

from turtle import Screen, Turtle


# creating a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping-Pong Game')
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up,'Up')
screen.onkey(go_down,'Down')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()