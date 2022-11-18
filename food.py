from turtle import Turtle #importa la libreria de turtle para el funcionamiento del juego
import random # importa la libreria de random para la aparicion de un objeto de manera aleatoria

class Food(Turtle): 

    def __init__(self):
        super().__init__()
        self.shape("circle") # Define la forma del objeto
        self.penup() # Para no dejar rastro de la linea del objeto

        self.color("blue") # Define el color del objeto
        self.speed("fastest") # Define la velocidad de reaparicion de la comida
        self.refresh() # Define que la comida debe reaparecer

    def refresh(self):
        random_x = random.randint(-280, 280) # Sirve para ubicar el objeto dentro de la venta de forma aleatoria en el eje x
        random_y = random.randint(-280, 280) # Sirve para ubicar el objeto dentro de la venta de forma aleatoria en el eje y
        self.goto(random_x, random_y) # Sirve para definir a que direcciones va el objetp