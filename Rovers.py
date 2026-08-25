



class Rover:
    def __init__(self, x, y, orientacion): 
        self.x = x
        self.y = y
        self.orientacion = orientacion

    def ejecutar_comando(self, comando):
        if comando == "F":
            self.avanza_una_celda()
        elif comando == "R":
            self.girar_derecha()
        elif comando == "L":
            self.girar_izquierda()
        elif comando == "B":
            self.retroceder_una_celda()

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

    def avanzar_una_celda(self):
        if self.orientacion == "Norte":
            self.y += 1
        elif self.orientacion == "Este":
            self.x += 1
        elif self.orientacion == "Sur":
            self.y -= 1
        elif self.orientacion == "Oeste":
            self.x -= 1

        return (self.x, self.y, self.orientacion)

    def retroceder_una_celda(self):
        if self.orientacion == "Norte":
            self.y -= 1
        elif self.orientacion == "Sur":
            self.y += 1
        elif self.orientacion == "Este":
            self.x -= 1
        elif self.orientacion == "Oeste":
            self.x += 1

        return (self.x, self.y, self.orientacion)
   