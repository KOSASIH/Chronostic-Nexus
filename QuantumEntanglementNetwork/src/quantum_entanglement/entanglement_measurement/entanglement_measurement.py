import numpy as np
from qiskit import QuantumCircuit, execute
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import QFT

class EntanglementMeasurement:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def measure_entanglement(self):
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def measure_w_state(self):
        self.circuit.x(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def measure_ghz_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def measure_cluster_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(1, 2)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def measure_graph_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(1, 2)
        self.circuit.cx(2, 0)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class EntanglementMeasurementSwapping(EntanglementMeasurement):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_swapping_measurement(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class EntanglementMeasurementPurification(EntanglementMeasurement):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_purification_measurement(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class EntanglementMeasurementConcentration(EntanglementMeasurement):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_concentration_measurement(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class EntanglementMeasurementDilution(EntanglementMeasurement):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_dilution_measurement(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts
