from turtle import Turtle

SCREEN_HEIGHT = 700
FONT_SIZE = 20
Y_POSITION = int(SCREEN_HEIGHT / 2 * 0.9)
ALIGNMENT = "center"
FONT = ("Courier", FONT_SIZE, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, Y_POSITION)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, Y_POSITION)
        self.update_score()

    def back_to_zero(self):
        self.score = 0
        self.clear()
        self.goto(0, Y_POSITION)
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
