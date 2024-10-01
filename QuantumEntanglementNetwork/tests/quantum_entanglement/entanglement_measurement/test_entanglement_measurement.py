import unittest
from quantum_entanglement.entanglement_measurement import EntanglementMeasurement

class TestEntanglementMeasurement(unittest.TestCase):
    def test_entanglement_measurement(self):
        entanglement_measurement = EntanglementMeasurement(2)
        entanglement_measurement.measure_entanglement()
        self.assertIsNotNone(entanglement_measurement.circuit)

    def test_w_state_measurement(self):
        entanglement_measurement = EntanglementMeasurement(3)
        entanglement_measurement.measure_w_state()
        self.assertIsNotNone(entanglement_measurement.circuit)

    def test_ghz_state_measurement(self):
        entanglement_measurement = EntanglementMeasurement(3)
        entanglement_measurement.measure_ghz_state()
        self.assertIsNotNone(entanglement_measurement.circuit)

    def test_cluster_state_measurement(self):
        entanglement_measurement = EntanglementMeasurement(3)
        entanglement_measurement.measure_cluster_state()
        self.assertIsNotNone(entanglement_measurement.circuit)

    def test_graph_state_measurement(self):
        entanglement_measurement = EntanglementMeasurement(3)
        entanglement_measurement.measure_graph_state()
        self.assertIsNotNone(entanglement_measurement.circuit)

if __name__ == '__main__':
    unittest.main()
