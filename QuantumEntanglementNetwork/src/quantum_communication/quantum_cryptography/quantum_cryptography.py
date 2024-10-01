import numpy as np
from qiskit import QuantumCircuit, execute
from qiskit.quantum_info import Statevector
from qiskit.circuit.library import QFT

class QuantumCryptography:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits)

    def bb84_protocol(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def ekert91_protocol(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def bennett92_protocol(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def dense_coding(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

    def superdense_coding(self):
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.circuit.cx(0, 2)
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class QuantumCryptographySwapping(QuantumCryptography):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_swapping_cryptography(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class QuantumCryptographyPurification(QuantumCryptography):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_purification_cryptography(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class QuantumCryptographyConcentration(QuantumCryptography):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_concentration_cryptography(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts

class QuantumCryptographyDilution(QuantumCryptography):
    def __init__(self, num_qubits):
        super().__init__(num_qubits)

    def entanglement_dilution_cryptography(self, qubits):
        self.circuit.cx(qubits[0], qubits[1])
        self.circuit.cx(qubits[1], qubits[2])
        self.circuit.cx(qubits[2], qubits[3])
        self.circuit.measure_all()
        job = execute(self.circuit, backend='qasm_simulator')
        result = job.result()
        counts = result.get_counts(self.circuit)
        return counts
