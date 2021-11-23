from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# adjusting the canvas settings
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.bgcolor('black')

# creating snake object and controlling it with the help of user input
screen.tracer(0)
snake = Snake(3)
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update() detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with snake body(blocks)
    # if snake.head collides with any segment in the tail:
        #game over
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
