import time
from turtle import Screen
from food import Food
from scoreboard import Score

from snake import Snake


if __name__ == '__main__':


    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")



    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            score.scoring()
            snake.extend()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over()

        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()


    screen.exitonclick()