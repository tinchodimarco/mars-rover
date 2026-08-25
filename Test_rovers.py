from Rovers import Rover 
import pytest



def test_informa_posicion():
  rover = Rover(0, 0, "Norte")

  assert rover.x == (0)
  assert rover.y == (0)
  assert rover.orientacion == ("Norte")

def test_girar_derecha():
  rover = Rover(0, 0, "Norte")
  rover.girar_derecha()

  assert rover.x == (0)
  assert rover.y == (0)
  assert rover.orientacion == ("Este")

def test_girar_izquierda():
  rover = Rover(0, 0, "Norte")
  rover.girar_izquierda()

  assert rover.x == (0)
  assert rover.y == (0)
  assert rover.orientacion == ("Oeste")

def test_avanzar_una_celda():
  rover = Rover(0, 0, "Norte")
  rover.avanzar_una_celda()

  assert rover.x == (0)
  assert rover.y == (1)
  assert rover.orientacion == ("Norte")

def test_retroceder_una_celda():
  rover = Rover(0, 0, "Norte")
  rover.retroceder_una_celda()

  assert rover.x == 0
  assert rover.y == -1
  assert rover.orientacion == "Norte"
