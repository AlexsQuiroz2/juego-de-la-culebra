from turtle import Turtle #importa la libreria de turtle para el funcionamiento del juego

STARTING_POSITIONS = [(0, 0), (20, 0), (20,0)] # ALmacena las direcciones dentro de una variable
MOVE_DISTANCE = 20 # Define el movimiento del objeto
UP = 90 # Define el giro del objeto hacia arriba
DOWN = 270 # Define el giro del objeto hacia abajo
LEFT = 180 # Define el giro del objeto hacia la izquierda
RIGHT = 0 # Define el giro del objeto hacia la derecha

class Snake:

    def __init__(self):
        self.segments = [] # sirve para guardar cada segmento
        self.create_snake() # sirve para crear el objeto "serpiente"
        self.head = self.segments[0] # guarda los dos datos anteriores dentro de un mismo objeto

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position) #define la posicion inicial del objeto

    def add_segment(self, position):
        new_segment = Turtle("turtle") # DEfine la figura del objeto
        new_segment.color("lawngreen") # Deine el color del objeto
        new_segment.penup() # Elimina el rastro del objeto
        new_segment.goto(position) # Define la posicion del objeto
        self.segments.append(new_segment) # Agrega todo lo anterior al objeto

    # Funcionalidad del objeto
    
    def extend(self):

        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)- 1, 0, -1):

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)