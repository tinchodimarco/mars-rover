



class Rover:
    def __init__(self, x, y, orientacion): 
        self.x = x
        self.y = y
        self.orientacion = orientacion


def informa_posicion():
    rover = Rover(0, 0, "Norte")
    return (rover.x, rover.y, rover.orientacion)
