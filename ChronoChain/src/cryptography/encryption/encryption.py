import hashlib
import random
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Encryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def generate_keys(self):
        return self.private_key, self.public_key

    def encrypt(self, data):
        encrypted_data = self.public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_data.decode()

class SymmetricEncryption:
    def __init__(self):
        self.key = hashlib.sha256(str(random.random()).encode()).hexdigest()

    def encrypt(self, data):
        encrypted_data = ""
        for i in range(len(data)):
            encrypted_data += chr(ord(data[i]) + ord(self.key[i % len(self.key)]))
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for i in range(len(encrypted_data)):
            decrypted_data += chr(ord(encrypted_data[i]) - ord(self.key[i % len(self.key)]))
        return decrypted_data

class AsymmetricEncryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def generate_keys(self):
        return self.private_key, self.public_key

    def encrypt(self, data):
        encrypted_data = self.public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_data.decode()

class HashEncryption:
    def __init__(self):
        self.hash_function = hashlib.sha256()

    def encrypt(self, data):
        encrypted_data = self.hash_function.update(data.encode()).hexdigest()
        return encrypted_data

    def decrypt(self, encrypted_data):
        # Hash encryption is one-way, so decryption is not possible
        return None
