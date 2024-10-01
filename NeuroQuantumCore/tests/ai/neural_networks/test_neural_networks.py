import unittest
from neural_networks.neural_networks import NeuralNetwork

class TestNeuralNetworks(unittest.TestCase):
    def test_neural_network(self):
        neural_network = NeuralNetwork (2, 2, 1)
        self.assertIsNotNone(neural_network.weights)

    def test_train(self):
        neural_network = NeuralNetwork(2, 2, 1)
        neural_network.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
        self.assertIsNotNone(neural_network.weights)

    def test_predict(self):
        neural_network = NeuralNetwork(2, 2, 1)
        neural_network.train([[0, 0], [0, 1], [1, 0], [1, 1]], [[0], [1], [1], [0]])
        self.assertIsNotNone(neural_network.predict([0, 0]))

if __name__ == '__main__':
    unittest.main()
