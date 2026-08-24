



class Rover:
    def __init__(self, x, y, orientacion): 
        self.x = x
        self.y = y
        self.orientacion = orientacion


    def informa_posicion(self):
        return (self.x, self.y, self.orientacion)

    def girar_derecha(self):
     
        if self.orientacion == "Norte":
         self.orientacion = "Este"
        elif self.orientacion == "Este":
            self.orientacion = "Sur"
        elif self.orientacion == "Sur":
         self.orientacion = "Oeste"
        elif self.orientacion == "Oeste":
         self.orientacion = "Norte"
        return (self.x, self.y, self.orientacion)

    def girar_izquierda(self): 
        if self.orientacion == "Norte":
          self.orientacion = "Oeste"
        elif self.orientacion == "Oeste":
         self.orientacion = "Sur"
        elif self.orientacion == "Sur":
         self.orientacion = "Este"
        elif self.orientacion == "Este":
         self.orientacion = "Norte"
        return (self.x, self.y, self.orientacion)

    
   