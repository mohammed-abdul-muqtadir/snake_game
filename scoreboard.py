from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.colition(0)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=('Arial', 24, 'normal'))

    def colition(self, num):
        if num == 1:
            self.score += 1
        self.clear()

        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))
