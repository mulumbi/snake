# Mock up of the snake game on old Nokia phones

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import keyboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)
screen.title("Snakey Snake Game")
screen.tracer(0)

# setting up my snake body
hiss = Snake()
munch = Food()
board = ScoreBoard()
game_is_on = board.game_state

screen.listen()
screen.onkey(hiss.up, "Up")
screen.onkey(hiss.down, "Down")
screen.onkey(hiss.left, "Left")
screen.onkey(hiss.right, "Right")

# move the snake continuously
# make the last seg move to where the prev was then only control the first
while game_is_on:
    hiss.move_forward()
    screen.update()
    time.sleep(0.1)
    # detect collision with food
    if hiss.head.distance(munch) < 15:
        hiss.grow()
        munch.teleport()
        board.update_score()

    # detect collision with wall
    hx = hiss.head.xcor()
    hy = hiss.head.ycor()
    head_xstate = False
    head_ystate = False
    if hx < -295 or hx > 295:
        head_xstate = True
    if hy < -295 or hy > 295:
        head_ystate = True
    if head_xstate or head_ystate:
        board.reset_score()
        hiss.reset_snake()

    # detect collision with body (check if snake bites itself)
    for seg in hiss.body[1:]:
        if hiss.head.distance(seg) < 10:
            board.reset_score()
            hiss.reset_snake()

    # detect when user wants to end the game
    if keyboard.is_pressed('x'):
        board.game_over()
        game_is_on = board.game_state

screen.exitonclick()
