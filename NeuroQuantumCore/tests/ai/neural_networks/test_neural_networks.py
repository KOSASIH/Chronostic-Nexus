import unittest
from neural_networks import NeuralNetwork

class TestNeuralNetworks(unittest.TestCase):
    def test_neural_network(self):
        nn = NeuralNetwork((784,), 10)
        self.assertEqual(nn.input_shape, (784,))
        self.assertEqual(nn.num_classes, 10)

    def test_train(self):
        nn = NeuralNetwork((784,), 10)
        X_train = np.random.rand(100, 784)
        y_train = np.random.randint(0, 10, 100)
        nn.train(X_train, y_train)
        self.assertIsNotNone(nn.model)

    def test_evaluate(self):
        nn = NeuralNetwork((784,), 10)
        X_test = np.random.rand(100, 784)
        y_test = np.random.randint(0, 10, 100)
        loss, accuracy = nn.evaluate(X_test, y_test)
        self.assertGreaterEqual(accuracy, 0)
        self.assertLessEqual(accuracy, 1)

    def test_predict(self):
        nn = NeuralNetwork((784,), 10)
        X = np.random.rand(1, 784)
        prediction = nn.predict(X)
        self.assertEqual(prediction.shape, (1, 10))

if __name__ == '__main__':
    unittest.main()
