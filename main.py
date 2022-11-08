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
from paddle import Paddle
from ball import Ball
import time

# creating a screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping-Pong Game')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.07)
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 and ball.heading() == 0:
        ball.bounce_right()
    elif ball.ycor() > 280 and ball.heading() == 90:
        ball.bounce_left()
    elif ball.ycor() < -280 and ball.heading() == 180:
        ball.bounce_right()
    elif ball.ycor() < -280 and ball.heading() == 270:
        ball.bounce_left()
    else:
        pass

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        if ball.heading() == 270 or ball.heading() == 90:
            ball.bounce_right()
        elif ball.heading() == 0 or ball.heading() == 180:
            ball.bounce_left()
        else:
            pass

    # If paddle misses the paddle, the ball should restart from the center position again, giving opposite player score
    if ball.xcor() > 390:
        # Add a score class
        ball.reset_position()


    if ball.xcor() < -390:
        # Add a score class here
        ball.reset_position()



screen.exitonclick()