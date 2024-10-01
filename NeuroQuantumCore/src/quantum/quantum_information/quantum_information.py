import numpy as np
from qiskit import QuantumCircuit, execute

class QuantumInformation:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def add_gate(self, gate, qubit):
        self.circuit.append(gate, [qubit])

    def measure(self, qubit):
        self.circuit.measure(qubit, qubit)

    def run(self):
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class QuantumTeleportation(QuantumInformation):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def teleport(self):
        self.add_gate('H', 0)
        self.add_gate('CNOT', 0, 1)
        self.add_gate('H', 1)
        self.measure(0)
        self.measure(1)
        return self.run()

class QuantumSuperdenseCoding(QuantumInformation):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def superdense_coding(self):
        self.add_gate('H', 0)
        self.add_gate('CNOT', 0, 1)
        self.add_gate('H', 1)
        self.measure(0)
        self.measure(1)
        return self.run()

    def decode(self):
        self.add_gate('H', 0)
        self.add_gate('CNOT', 0, 1)
        self.add_gate('H', 1)
        self.measure(0)
        self.measure(1)
        return self.run()
