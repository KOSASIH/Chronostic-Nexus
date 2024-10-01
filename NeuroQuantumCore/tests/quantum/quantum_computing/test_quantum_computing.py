import unittest
from quantum_computing.quantum_computing import QuantumComputer

class TestQuantumComputing(unittest.TestCase):
    def test_quantum_computer(self):
        quantum_computer = QuantumComputer(2)
        self.assertIsNotNone(quantum_computer.circuit)

    def test_add_gate(self):
        quantum_computer = QuantumComputer(2)
        quantum_computer.add_gate("H", 0)
        self.assertIn("H", quantum_computer.circuit.gates)

    def test_measure(self):
        quantum_computer = QuantumComputer(2)
        quantum_computer.measure(0)
        self.assertIsNotNone(quantum_computer.circuit.measurements)

if __name__ == '__main__':
    unittest.main()
