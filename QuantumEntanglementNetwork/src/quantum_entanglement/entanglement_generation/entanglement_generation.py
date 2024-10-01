import numpy as np
from qiskit import QuantumCircuit, execute
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import QFT

class EntanglementGeneration:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def generate_entanglement(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        return self.circuit

    def generate_w_state(self):
        self.circuit.x(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        return self.circuit

    def generate_ghz_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        return self.circuit

    def generate_cluster_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(1, 2)
        return self.circuit

    def generate_graph_state(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(1, 2)
        self.circuit.cx(2, 0)
        return self.circuit

class EntanglementGenerationSwapping(EntanglementGeneration):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_swapping(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        return self.circuit

class EntanglementGenerationPurification(EntanglementGeneration):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_purification(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class EntanglementGenerationConcentration(EntanglementGeneration):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_concentration(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class EntanglementGenerationDilution(EntanglementGeneration):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_dilution(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts
