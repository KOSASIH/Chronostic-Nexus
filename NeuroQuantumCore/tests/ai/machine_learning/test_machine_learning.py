import unittest
from machine_learning.machine_learning import MachineLearning

class TestMachineLearning(unittest.TestCase):
    def test_machine_learning(self):
        machine_learning = MachineLearning()
        self.assertIsNotNone(machine_learning.model)

    def test_train(self):
        machine_learning = MachineLearning()
        machine_learning.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
        self.assertIsNotNone(machine_learning.model)

    def test_predict(self):
        machine_learning = MachineLearning()
        machine_learning.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
        self.assertIsNotNone(machine_learning.predict([0, 0]))

if __name__ == '__main__':
    unittest.main()
