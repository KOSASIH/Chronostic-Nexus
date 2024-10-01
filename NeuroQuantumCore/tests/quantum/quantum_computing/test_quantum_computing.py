import unittest
from quantum_computing import QuantumComputer

class TestQuantumComputing(unittest.TestCase):
    def test_quantum_computer(self):
        qc = QuantumComputer(2)
        self.assertEqual(qc.num_qubits, 2)

    def test_add_gate(self):
        qc = QuantumComputer(2)
        qc.add_gate('H', 0)
        self.assertIn('H', qc.circuit)

    def test_measure(self):
        qc = QuantumComputer(2)
        qc.measure(0)
        self.assertIn('measure', qc.circuit)

    def test_run(self):
        qc = QuantumComputer(2)
        qc.add_gate('H', 0)
        qc.measure(0)
        result = qc.run()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
