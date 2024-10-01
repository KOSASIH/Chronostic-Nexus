import unittest
from cryptography.encryption import Encryption

class TestEncryption(unittest.TestCase):
    def test_encrypt(self):
        encryption = Encryption()
        data = "Hello, World!"
        encrypted_data = encryption.encrypt(data)
        self.assertIsNotNone(encrypted_data)

    def test_decrypt(self):
        encryption = Encryption()
        data = "Hello, World!"
        encrypted_data = encryption.encrypt(data)
        decrypted_data = encryption.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

if __name__ == '__main__':
    unittest.main()
