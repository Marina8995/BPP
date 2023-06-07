import unittest
import funciones

class TestFunciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(funciones.suma(2, 2), 4)
        self.assertEqual(funciones.suma(1, 2), 4)
        self.assertEqual(funciones.suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(funciones.resta(5, 2), 3)
        self.assertEqual(funciones.resta(1, 2), 4)
        self.assertEqual(funciones.resta(0, 0), 0)

    def test_multiplicacion(self):
        self.assertEqual(funciones.multiplicacion(2, 3), 6)
        self.assertEqual(funciones.multiplicacion(1, 2), 4)
        self.assertEqual(funciones.multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(funciones.division(10, 2), 5)
        self.assertEqual(funciones.division(8, 0), 4)
        with self.assertRaises(ValueError):
            funciones.division(4, 0)     