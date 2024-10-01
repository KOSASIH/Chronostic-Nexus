# graviton_based_storage_main.py

from graviton_based_storage import GravitonBasedStorage
from graviton_based_storage_utils import encode_data, decode_data, store_data, retrieve_data

def main():
    num_qubits = 10
    num_data_qubits = 5
    data = np.array([1, 0, 1, 0, 1])

    # Create a GravitonBasedStorage object
    gbs = GravitonBasedStorage(num_qubits, num_data_qubits)

    # Store the data using the GBS
    gbs.store(data)

    # Retrieve the stored data using the GBS
    retrieved_data = gbs.retrieve()
    print(retrieved_data)

if __name__ == '__main__':
    main()
