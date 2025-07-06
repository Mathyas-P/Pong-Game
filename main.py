from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard,WINNING_POINT
from divider import Divider


screen=Screen()
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
scoreboard=ScoreBoard()
divider=Divider()


left_paddle=Paddle(position=(-350,0))
right_paddle=Paddle(position=(350,0))

screen.listen()
screen.onkeypress(right_paddle.go_up,"Up")
screen.onkeypress(right_paddle.go_down,"Down")
screen.onkeypress(left_paddle.go_up,"w")
screen.onkeypress(left_paddle.go_down,"s")
game_on=True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.movement()

    #Detect collision on wall

    if ball.ycor()>279 or ball.ycor()<-275:
        ball.bounce_y()

    if ball.distance(right_paddle)<50 and ball.xcor()>320 or ball.distance(left_paddle)<50 and ball.xcor()<-320:
         ball.bounce_x()

    #Right paddle
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.add_left_point()


    #Left paddle
    if ball.xcor()<-390:
        ball.reset_position()
        scoreboard.add_right_point()

    if scoreboard.left_score==WINNING_POINT or scoreboard.right_score==WINNING_POINT:
        game_on=False
        scoreboard.winner()







screen.exitonclick()