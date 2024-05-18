import unittest
from triangulo import calcular_area_triangulo


class TestCalculoAreaTriangulo(unittest.TestCase):

    def test_area_valida(self):
        self.assertAlmostEqual(calcular_area_triangulo(3, 4, 5), 6.0)
        self.assertAlmostEqual(calcular_area_triangulo(7, 10, 5), 16.24807680927192)
        self.assertAlmostEqual(calcular_area_triangulo(6, 8, 10), 24.0)

    def test_lados_invalidos(self):
        with self.assertRaises(ValueError):
                calcular_area_triangulo(1, 2, 3)

    def test_lados_negativos(self):
        with self.assertRaises(ValueError):
            calcular_area_triangulo(-3, 4, 5)

    def test_lados_cero(self):
        with self.assertRaises(ValueError):
            calcular_area_triangulo(0, 4, 5)


if __name__ == '__main__':
    unittest.main()
