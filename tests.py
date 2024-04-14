import unittest
from vocales import contar_vocales


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales("zzz")
        self.assertAlmostEqual(resultado,{})

    def test_contar_a(self):
        resultado = contar_vocales("cas")
        self.assertAlmostEqual(resultado,{"a": 1})

    def test_contar_aa(self):
        resultado = contar_vocales("casa")
        self.assertAlmostEqual(resultado,{"a": 2})
    
    def test_contar_bese(self):
        resultado = contar_vocales("bese")
        self.assertAlmostEqual(resultado,{"e": 2})

    def test_contar_besa(self):
        resultado = contar_vocales("besa")
        self.assertAlmostEqual(resultado,{"a" : 1, "e" : 1 })

    def test_contar_casanova(self):
        resultado = contar_vocales("casanova")
        self.assertAlmostEqual(resultado,{"a": 3, "o" : 1})

    def test_contar_murciElago(self):
        resultado = contar_vocales("murciElago")
        self.assertAlmostEqual(resultado,{"a": 3, "o" : 1})
        
unittest.main()