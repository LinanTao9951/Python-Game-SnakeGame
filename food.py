from turtle import Turtle
import random

WIDTH = 20

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-300 + WIDTH, 300 - WIDTH)
        random_y = random.randint(-300 + WIDTH, 300 - WIDTH)
        self.goto(random_x, random_y)
