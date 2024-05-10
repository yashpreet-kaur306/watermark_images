from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        """Updates scoreboard on the screen."""
        self.clear()
        self.goto(150, 265)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 10, "normal"))
        self.goto(-260, 265)
        self.write(f"Lives:{self.lives}", align="center", font=("Courier", 10, "normal"))
        self.goto(260, 265)
        self.write(f"Highscore:{self.highscore}", align="center", font=("Courier", 10, "normal"))


    def reset(self):
        """Manage highscore throughout the game."""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.update_scoreboard()

    def add_points(self, level_score):
        """Adds scores as ball collide with bricks."""
        self.score += level_score
        self.update_scoreboard()

    def lives_left(self):
        """Chances left to play."""
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        if self.lives == 0:
            self.goto(0, 0)
            self.write("Game over", align="center", font=("Courier", 15, "normal"))
            self.goto(0, -50)
            self.write(f"Highscore:{self.highscore}", align="center", font=("Courier", 15, "normal"))
            return True
        else:
            return False
