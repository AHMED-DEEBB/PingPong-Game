# import turtle module
# it's a module make me able to draw shapes and make it move

import turtle

# create window that displays the game
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)           # to prevent screen from updating automatically and make me able to control the game speed

#  paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.color("blue")
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

#  paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.color("red")
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()     # stop object from drawing lines while moving
paddle2.goto(350, 0)        # set the position of the object

#  ball
ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 260)
score.hideturtle()
score.write("Player 1: 0  player 2: 0", align="center", font=("Courier", 24, "normal"))

#fuctions
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# keyboard bindings

wind.listen()      # tell the window to expect input
wind.onkeypress(paddle1_up, "w")
wind.onkeypress(paddle1_down, "s")
wind.onkeypress(paddle2_up, "Up")
wind.onkeypress(paddle2_down, "Down")



#  Main game loop
while True:
    wind.update()

    #  ball movement
    ball.setx(ball.xcor() + ball.dx)    # ball starts at 0 every time loop runs x-axis will increase by ball.dx value
    ball.sety(ball.ycor() + ball.dy)    # ball starts at 0 every time loop runs y-axis will increase by ball.dy value

    #  border check , top border is +300, bottom is -300, ball is 20px
    if ball.ycor() > 290:    # if ball is at the top border
        ball.sety(290)       # set y coordinates +290
        ball.dy *= -1        # reverse y direction

    if ball.ycor() < -290:   # if ball is at the bottom border
        ball.sety(-290)      # set y coordinates -290
        ball.dy *= -1        # reverse y direction

    if ball.xcor() > 390:    # if the ball is at the right border
        ball.goto(0, 0)      # return to the origin
        ball.dx *= -1        # reverse x direction
        score.clear()
        score1 += 1
        score.write("Player 1: {}  player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:   # if the ball is at the right border
        ball.goto(0, 0)      # return to the origin
        ball.dx *= -1        # reverse x direction
        score.clear()
        score2 += 1
        score.write("Player 1: {}  player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # ball hitting paddles
    if (340 < ball.xcor() < 350) and (paddle2.ycor() + 40 > ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle1.ycor() + 40 > ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
