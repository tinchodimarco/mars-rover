from Rovers import Rover 
import pytest



def test_informa_posicion():
  rover = Rover(0, 0, "Norte")

  assert rover.x == (0)
  assert rover.y == (0)
  assert rover.orientacion == ("Norte")
