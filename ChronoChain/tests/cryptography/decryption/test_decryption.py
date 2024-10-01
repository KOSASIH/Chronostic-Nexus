import unittest
from cryptography.decryption import Decryption

class TestDecryption(unittest.TestCase):
    def test_decrypt(self):
        decryption = Decryption()
        data = "Hello, World!"
        encrypted_data = decryption.encrypt(data)
        decrypted_data = decryption.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
