from Rovers import Rover 
import pytest



def test_informa_posicion():
  rover = Rover(0, 0, "Norte")

  assert rover.x == (0)
  assert rover.y == (0)
  assert rover.orientacion == ("Norte")

def test_girar_izquierda():
    rover = Rover(0, 0, "Norte")
    rover.girar_izquierda()
    assert rover.x == (0)
    assert rover.y == (0)
    assert rover.orientacion == ("Oeste")

def test_girar_derecha():
      rover = Rover(0, 0, "Norte")
      rover.girar_derecha()
      assert rover.x == (0)
      assert rover.y == (0)
      assert rover.orientacion == ("Este")
