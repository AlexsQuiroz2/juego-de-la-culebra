from turtle import Screen  # Desde la libreria Turtle importa el screen 
from snake import Snake    # Llama el archvo snake y importa la clase Snake
from food import Food     # Llama el archvo food y importa la clase Food
from scoreboard import Scoreboard   # Llama el archvo scoreboard y importa la clase Scoreboard
import time #reconoce en tiempo real el juego, desde el inicio hasta el final

#creacion de la ventana

screen = Screen()   # Llama un screen
screen.setup(width=600, height=600) # Crea los limites de la ventana
screen.bgcolor("white") #cambia el color del fondo de la ventana
screen.title("My Snake Game")   # nombre el titulo
screen.tracer(0)  # reconoce la animacion de la libreria de turtle


# Funcionabilidad del juego

snake = Snake() # Llama la clase snake
food = Food() # Llama la clase food
scoreboard = Scoreboard() # Llama la clase scoreboars

screen.listen() #Especifica el número de conexiones no aceptadas que el sistema permitirá antes de rechazar nuevas conexiones.
screen.onkey(snake.up, "Up")    # vincula el evento de liberacion de la tecla superior
screen.onkey(snake.down, "Down") # vincula el evento de liberacion de la tecla inferior
screen.onkey(snake.left, "Left") # vincula el evento de liberacion de la tecla izquierda
screen.onkey(snake.right, "Right")  # vincula el evento de liberacion de la tecla derecha

game_is_on = True
while game_is_on:
    screen.update() # inserta los elementos especificados en el diccionario.
    time.sleep(0.9) # detecta la velocidad a la que se mueve el objeto
    snake.move() # se utiliza para mover un archivo de un directorio a otro.

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh() # Vuelve a crear el objeto de la comida
        snake.extend()  # Al consumir la comida
        scoreboard.increase_score() # Cunado consume la comida el puntaje aumenta de a 1 unidad

    #Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -319 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
        game_is_on = False
        scoreboard.game_over() # termina el juego cunado detecte una colision con un borde del muro.

#Detect collision with tail.
for segment in snake.segments:
    if segment == snake.head:
        pass
    elif snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over() # termina el juego cunado detecta la colision con el mismo cuerpo del objeto

screen.exitonclick()