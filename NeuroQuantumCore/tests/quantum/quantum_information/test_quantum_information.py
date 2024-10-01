import unittest
from quantum_information import QuantumInformation

class TestQuantumInformation(unittest.TestCase):
    def test_quantum_information(self):
        qi = QuantumInformation(2)
        self.assertEqual(qi.num_qubits, 2)

    def test_add_gate(self):
        qi = QuantumInformation(2)
        qi.add_gate('H', 0)
        self.assertIn('H', qi.circuit)

    def test_measure(self):
        qi = QuantumInformation(2)
        qi.measure(0)
        self.assertIn('measure', qi.circuit)

    def test_run(self):
        qi = QuantumInformation(2)
        qi.add_gate('H', 0)
        qi.measure(0)
        result = qi.run()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
