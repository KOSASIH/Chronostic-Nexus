import unittest
from deep_learning import DeepLearningModel

class TestDeepLearning(unittest.TestCase):
    def test_deep_learning_model(self):
        dl = DeepLearningModel((784,), 10)
        self.assertEqual(dl.input_shape, (784,))
        self.assertEqual(dl.num_classes, 10)

    def test_train(self):
        dl = DeepLearningModel((784,), 10)
        X_train = np.random.rand(100, 784)
        y_train = np.random.randint(0, 10, 100)
        dl.train(X_train, y_train)
        self.assertIsNotNone(dl.model)

    def test_evaluate(self):
        dl = DeepLearningModel((784,), 10)
        X_test = np.random.rand(100, 784)
        y_test = np.random.randint(0, 10, 100)
        loss, accuracy = dl.evaluate(X_test, y_test)
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)

    def test_predict(self):
        dl = DeepLearningModel((784,), 10)
        X = np.random.rand(1, 784)
        prediction = dl.predict(X)
        self.assertEqual(prediction.shape, (1, 10))

if __name__ == '__main__':
    unittest.main()
