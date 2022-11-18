from turtle import Screen  # Desde la libreria Turtle importa el screen 
from snake import Snake    # Llama el archvo snake y importa la clase Snake
from food import Food     # Llama el archvo food y importa la clase Food
from scoreboard import Scoreboard   # Llama el archvo scoreboard y importa la clase Scoreboard
import time

screen = Screen()   # Llama un screen
screen.setup(width=600, height=600) # Crea los limites de la ventana
screen.bgcolor("white")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -319 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        game_is_on = False
        scoreboard.game_over()

#Detect collision with tail.
for segment in snake.segments:
    if segment == snake.head:
        pass
    elif snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()