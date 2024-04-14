import unittest
from vocales import contar_vocales


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales("zzz")
        self.assertAlmostEqual(resultado,{})

    def test_contar_a(self):
        resultado = contar_vocales("cas")
        self.assertAlmostEqual(resultado,{"a", 1})

    def test_contar_aa(self):
        resultado = contar_vocales("casa")
        self.assertAlmostEqual(resultado,{"a", 2})
    
    def test_contar_bc(self):
        resultado = contar_vocales("casa")
        self.assertAlmostEqual(resultado,{"a", 2})

    def test_contar_bc(self):
        resultado = contar_vocales("casa")
        self.assertAlmostEqual(resultado,{"a", 2})
unittest.main()