import pytest
import funciones

def test_suma():
    assert funciones.suma(2, 3) == 5
    assert funciones.suma(-5, 8) == 3
    assert funciones.suma(0, 0) == 0

def test_restar():
    assert funciones.resta(5, 3) == 2
    assert funciones.resta(10, 7) == 3
    assert funciones.resta(0, 0) == 0

def test_multiplicar():
    assert funciones.multiplicacion(2, 3) == 6
    assert funciones.multiplicacion(-5, 8) == -40
    assert funciones.multiplicacion(0, 10) == 0

def test_dividir():
    assert funciones.division(10, 2) == 5
    assert funciones.division(8, 4) == 2
    with pytest.raises(ValueError):
        funciones.division(5, 0)