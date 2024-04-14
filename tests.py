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
        self.assertAlmostEqual(resultado,{"u": 1, "o" : 1, "a" : 1, "E" : 1, "i" : 1})
#mayusculas
    def test_contar_A(self):
        resultado = contar_vocales("cAs")
        self.assertAlmostEqual(resultado,{"A": 1})
    def test_contar_AA(self):
        resultado = contar_vocales("cAsA")
        self.assertAlmostEqual(resultado,{"A": 2})
    
    def test_contar_bEsE(self):
        resultado = contar_vocales("bEsE")
        self.assertAlmostEqual(resultado,{"E": 2})

    def test_contar_bEsA(self):
        resultado = contar_vocales("bEsA")
        self.assertAlmostEqual(resultado,{"A" : 1, "E" : 1 })

    def test_contar_cAsAnOvA(self):
        resultado = contar_vocales("cAsAnOvA")
        self.assertAlmostEqual(resultado,{"A": 3, "O" : 1})

    def test_contar_mUrcIElAgO(self):
        resultado = contar_vocales("mUrcIElAgO")
        self.assertAlmostEqual(resultado,{"U": 1, "O" : 1, "A" : 1, "E" : 1, "I" : 1})


unittest.main()