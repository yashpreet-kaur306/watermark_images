from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

BLACK = "#28282B"
LEVEL1_COLOR = "#6082B6"
LEVEL2_COLOR = "#DFFF00"
LEVEL3_COLOR = "#32CD32"
LEVEL4_COLOR = "#E35335"
LEVEL5_COLOR = "#BB0909"

screen = Screen()
screen.bgcolor(BLACK)
screen.setup(width=750, height=600)
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
bricks = Bricks()
scoreboard = Scoreboard()

bricks.create_bricks((-350, 150), LEVEL1_COLOR)
bricks.create_bricks((-350, 173), LEVEL2_COLOR)
bricks.create_bricks((-350, 196), LEVEL3_COLOR)
bricks.create_bricks((-350, 218), LEVEL4_COLOR)
bricks.create_bricks((-350, 241), LEVEL5_COLOR)

screen.listen()
screen.onkeypress(paddle.slide_right, "Right")
screen.onkeypress(paddle.slide_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    paddle.check_boundary()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.bounce_x()

    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.lives_left()

    if paddle.detect_collision(ball):
        ball.bounce_y()

    all_levels = [0, 1, 2, 3, 4]
    for level in all_levels:
        current_level_bricks = bricks.get_current_level_bricks(level)
        for brick in current_level_bricks:
            if bricks.is_visible(brick) and ball.distance(brick) < 40:
                bricks.disappear_brick(brick)
                ball.bounce_x()
                points_map = {0: 20, 1: 45, 2: 65, 3: 85, 4: 100}
                if level in points_map:
                    scoreboard.add_points(points_map[level])
                    scoreboard.reset()
                break
        else:
            continue

        break

    if scoreboard.game_over():
        game_is_on = False


screen.exitonclick()
