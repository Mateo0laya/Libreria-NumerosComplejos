import ComplexOps as COps
import unittest

class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        self.assertAlmostEqual(COps.suma((1.2,-2),(-4,5)), (-2.8,3))

    def test_resta(self):
        self.assertAlmostEqual(COps.resta((100.5,26),(254,-9)), (-153.5,35))

    def test_producto(self):
        self.assertAlmostEqual(COps.producto((-2,5.2),(4,1)), (-13.2,18.8))

    def test_division(self):
        self.assertAlmostEqual(COps.division((-2,5.2),(4,1)), ((-2.8/17),(22.8/17)))

    def test_modulo(self):
        self.assertAlmostEqual(COps.modulo((-5,12)), (13))

    def test_conjugado(self):
        self.assertAlmostEqual(COps.conjugado((-23.1469,-95.321)), (-23.1469,95.321))

    def test_conversionac(self):
        self.assertAlmostEqual(COps.conversionac((2,45)), ((pow(2,0.5)),(pow(2,0.5))))

    def test_conversionap(self):
        self.assertAlmostEqual(COps.conversionap((7,-2)), ((pow(53,0.5)), -15.945395900922856))

    def test_fase(self):
        self.assertAlmostEqual(COps.fase((4,3)), (36.8698976))

if __name__ == '__main__':
    unittest.main()