from turtle import Screen, Turtle
import time

screen = Screen()

#creacion de la ventana
screen.setup(width=645, height=700)
screen.bgcolor("white")
screen.title("Snake game")

#movimiento
segments = []

#posision de la culebra
starting_position = [(0,0),(25,0),(50,0)]

for position in starting_position:
    new_segment = Turtle("turtle")
    new_segment.color("lawngreen")
    new_segment.penup()
    new_segment.goto(position)
    #movimiento
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg in segments:
        seg.forward(25)
        seg.left(35) 


screen.exitonclick()