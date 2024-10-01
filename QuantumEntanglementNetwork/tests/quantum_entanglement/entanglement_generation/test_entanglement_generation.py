import unittest
from quantum_entanglement.entanglement_generation import EntanglementGeneration

class TestEntanglementGeneration(unittest.TestCase):
    def test_entanglement_generation(self):
        entanglement_generation = EntanglementGeneration(2)
        entanglement_generation.generate_entanglement()
        self.assertIsNotNone(entanglement_generation.circuit)

    def test_w_state_generation(self):
        entanglement_generation = EntanglementGeneration(3)
        entanglement_generation.generate_w_state()
        self.assertIsNotNone(entanglement_generation.circuit)

    def test_ghz_state_generation(self):
        entanglement_generation = EntanglementGeneration(3)
        entanglement_generation.generate_ghz_state()
        self.assertIsNotNone(entanglement_generation.circuit)

    def test_cluster_state_generation(self):
        entanglement_generation = EntanglementGeneration(3)
        entanglement_generation.generate_cluster_state()
        self.assertIsNotNone(entanglement_generation.circuit)

    def test_graph_state_generation(self):
        entanglement_generation = EntanglementGeneration(3)
        entanglement_generation.generate_graph_state()
        self.assertIsNotNone(entanglement_generation.circuit)

if __name__ == '__main__':
    unittest.main()
