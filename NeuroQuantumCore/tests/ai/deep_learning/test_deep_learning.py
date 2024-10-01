import unittest
from deep_learning.deep_learning import DeepLearning

class TestDeepLearning(unittest.TestCase):
    def test_deep_learning(self):
        deep_learning = DeepLearning()
        self.assertIsNotNone(deep_learning.model)

    def test_train(self):
        deep_learning = DeepLearning()
        deep_learning.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
        self.assertIsNotNone(deep_learning.model)

    def test_predict(self):
        deep_learning = DeepLearning()
        deep_learning.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
        self.assertIsNotNone(deep_learning.predict([0, 0]))

if __name__ == '__main__':
    unittest.main()
