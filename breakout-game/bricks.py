from turtle import Turtle

class Bricks:
    def __init__(self):
        self.levels = []


    def create_bricks(self, position, color):
        """Create bricks"""
        level_bricks = []
        for i in range(12):
            brick = Turtle("square")
            brick.penup()
            brick.speed(10)
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.color(color)
            x_pos = position[0] + i * 63
            brick.setposition(x_pos, position[1])
            brick.visible = True
            level_bricks.append(brick)

        self.levels.append(level_bricks)
        return self.levels

    def disappear_brick(self, brick):
        brick.hideturtle()
        brick.visible = False

    def get_current_level_bricks(self, level):
        """Gets the current level of bricks being reached."""
        return self.levels[level]

    def is_visible(self, brick):
        return brick.visible
