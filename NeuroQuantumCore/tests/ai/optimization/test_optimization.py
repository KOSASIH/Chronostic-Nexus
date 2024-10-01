import unittest
from optimization.optimization import Optimization

class TestOptimization(unittest.TestCase):
    def test_optimization(self):
        optimization = Optimization()
        self.assertIsNotNone(optimization.function)

    def test_minimize(self):
        optimization = Optimization()
        optimization.minimize(lambda x: x**2)
        self.assertIsNotNone(optimization.minimum)

    def test_maximize(self):
        optimization = Optimization()
        optimization.maximize(lambda x: x**2)
        self.assertIsNotNone(optimization.maximum)

if __name__ == '__main__':
    unittest.main()
