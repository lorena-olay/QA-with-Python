import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Código para configurar el entorno de prueba
        self.string = "hello world"

    def test_upper(self):
        self.assertEqual(self.string.upper(), 'HELLO WORLD')

    def test_isupper(self):
        self.assertFalse(self.string.isupper())
        self.assertTrue('HELLO'.isupper())

    def tearDown(self):
        # Código para limpiar después de la prueba
        pass

if __name__ == '__main__':
    unittest.main()