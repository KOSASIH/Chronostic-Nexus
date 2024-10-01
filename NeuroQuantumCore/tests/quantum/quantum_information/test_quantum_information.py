import unittest
from quantum_information.quantum_information import QuantumInformation

class TestQuantumInformation(unittest.TestCase):
    def test_quantum_information(self):
        quantum_information = QuantumInformation(2)
        self.assertIsNotNone(quantum_information.circuit)

    def test_add_gate(self):
        quantum_information = QuantumInformation(2)
        quantum_information.add_gate("H", 0)
        self.assertIn("H", quantum_information.circuit.gates)

    def test_measure(self):
        quantum_information = QuantumInformation(2)
        quantum_information.measure(0)
        self.assertIsNotNone(quantum_information.circuit.measurements)

if __name__ == '__main__':
    unittest.main()
