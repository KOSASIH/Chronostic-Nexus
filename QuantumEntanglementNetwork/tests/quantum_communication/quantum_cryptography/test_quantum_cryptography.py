import unittest
from quantum_communication.quantum_cryptography import QuantumCryptography

class TestQuantumCryptography(unittest.TestCase):
    def test_quantum_cryptography(self):
        quantum_cryptography = QuantumCryptography(2)
        quantum_cryptography.bb84_protocol()
        self.assertIsNotNone(quantum_cryptography.circuit)

    def test_ekert91_protocol(self):
        quantum_cryptography = QuantumCryptography(3)
        quantum_cryptography.ekert91_protocol()
        self.assertIsNotNone(quantum_cryptography.circuit)

    def test_bennett92_protocol(self):
        quantum_cryptography = QuantumCryptography(3)
        quantum_cryptography.bennett92_protocol()
        self.assertIsNotNone(quantum_cryptography.circuit)

    def test_dense_coding(self):
        quantum_cryptography = QuantumCryptography(2)
       quantum_cryptography.dense_coding()
        self.assertIsNotNone(quantum_cryptography.circuit)

    def test_superdense_coding(self):
        quantum_cryptography = QuantumCryptography(3)
        quantum_cryptography.superdense_coding()
        self.assertIsNotNone(quantum_cryptography.circuit)

if __name__ == '__main__':
    unittest.main()
