from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("#6495ED")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.goto(0, -250)

    def slide_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def slide_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


    def detect_collision(self, ball):
        """Detect whether the paddle collided with ball or not."""
        if (self.ycor() - 15 < ball.ycor() < self.ycor() + 15) and (self.xcor() - 50 < ball.xcor() < self.xcor() + 50):
            return True
        else:
            return False

    def check_boundary(self):
        """Makes sure the paddle is within the boundary of screen."""
        if self.xcor() < -350:
            self.goto(-350, self.ycor())
        elif self.xcor() > 350:
            self.goto(350, self.ycor())
