from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
X_LIMIT = int(SCREEN_WIDTH / 2 - 5)
Y_LIMIT = int(SCREEN_HEIGHT / 2 - 5)

GAME_MODE = {"easy": 0.5, "normal": 0.2, "hard": 0.1, "super": 0.05}

# Create a screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

# Create a snake and a food
snake = Snake()
food = Food()
score = Scoreboard()
screen.update()

# Game mode selection by user
user_choice = screen.textinput(title="Choose a game mode", prompt="Input 'EASY', 'NORMAL', 'HARD', 'SUPER'").lower()
if user_choice in GAME_MODE.keys():
    game_mode = GAME_MODE[user_choice]
else:
    game_mode = GAME_MODE["normal"]

# Capture the key to control snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(game_mode)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with all
    if snake.head.xcor() > X_LIMIT or snake.head.xcor() < -X_LIMIT or snake.head.ycor() > X_LIMIT or snake.head.ycor() < -X_LIMIT:
        # Hit the wall
        is_on = False
        score.game_over()

    # Detect collision with tail

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            # Hit the tail
            is_on = False
            score.game_over()

screen.exitonclick()
