import unittest
from quantum_communication.quantum_key_distribution import QuantumKeyDistribution

class TestQuantumKeyDistribution(unittest.TestCase):
    def test_quantum_key_distribution(self):
        quantum_key_distribution = QuantumKeyDistribution(2)
        quantum_key_distribution.bb84_protocol()
        self.assertIsNotNone(quantum_key_distribution.circuit)

    def test_ekert91_protocol(self):
        quantum_key_distribution = QuantumKeyDistribution(3)
        quantum_key_distribution.ekert91_protocol()
        self.assertIsNotNone(quantum_key_distribution.circuit)

    def test_bennett92_protocol(self):
        quantum_key_distribution = QuantumKeyDistribution(3)
        quantum_key_distribution.bennett92_protocol()
        self.assertIsNotNone(quantum_key_distribution.circuit)

    def test_dense_coding(self):
        quantum_key_distribution = QuantumKeyDistribution(2)
        quantum_key_distribution.dense_coding()
        self.assertIsNotNone(quantum_key_distribution.circuit)

    def test_superdense_coding(self):
        quantum_key_distribution = QuantumKeyDistribution(3)
        quantum_key_distribution.superdense_coding()
        self.assertIsNotNone(quantum_key_distribution.circuit)

if __name__ == '__main__':
    unittest.main()
