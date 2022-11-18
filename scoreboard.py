from turtle import Turtle #importa la libreria de turtle para el funcionamiento del juego

ALIGNMENT = "center" # Define la ubicacion 
FONT = ("Comic sans", 24, "italic") # Define el tipo de letra y tamaño del titulo

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 # Define el valor por defecto del puntaje
        self.color("black") # Define el color del texto
        self.penup() # Para no dejar rastro de la linea del objeto
        self.goto(0, 270) # Define la ubicacion del texto
        self.hideturtle() # se utiliza para hacer que el objeto sea invisible.
        self.update_scoreboard() # Sirve para actializar el puntaje

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT) # Sirve para mostrar el texto "score"

    def game_over(self):
        self.goto(0, 0) # Ubicaion del texto
        self.write("GAME OVER",align=ALIGNMENT, font=FONT) # Sirve para mostrar el texto "Game over"

    def increase_score(self):
        self.score += 1 # sirve para aumnetar el valor del puntajo de uno en uno
        self.clear() # sirve para limpiar el anterior puntaje
        self.update_scoreboard() # actualiza el puntaje