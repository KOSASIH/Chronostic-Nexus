# graviton_based_storage_test.py

import unittest
from graviton_based_storage import GravitonBasedStorage
from graviton_based_storage_utils import encode_data, decode_data, store_data, retrieve_data

class TestGravitonBasedStorage(unittest.TestCase):
    def test_encode_data(self):
        num_qubits = 10
        num_data_qubits = 5
        data = np.array([1, 0, 1, 0, 1])
        qc = encode_data(data, num_qubits, num_data_qubits)
        self.assertEqual(qc.num_qubits, num_qubits)
        self.assertEqual(qc.num_clbits, num_data_qubits)

    def test_decode_data(self):
        num_qubits = 10
        num_data_qubits = 5
        data = np.array([1, 0, 1, 0, 1])
        qc = decode_data(data, num_qubits, num_data_qubits)
        self.assertEqual(qc.num_qubits, num_qubits)
        self.assertEqual(qc.num_clbits, num_data_qubits)

    def test_store_data(self):
        num_qubits = 10
        num_data_qubits = 5
        data = np.array([1, 0, 1, 0, 1])
        qc = store_data(data, num_qubits, num_data_qubits)
        self.assertEqual(qc.num_qubits, num_qubits)
        self.assertEqual(qc.num_clbits, num_data_qubits)

    def test_retrieve_data(self):
        num_qubits = 10
        num_data_qubits = 5
        data = np.array([1, 0, 1, 0, 1])
        qc = retrieve_data(num_qubits, num_data_qubits)
        self.assertEqual(qc.num_qubits, num_qubits)
        self.assertEqual(qc.num_clbits, num_data_qubits)

if __name__ == '__main__':
    unittest.main()
