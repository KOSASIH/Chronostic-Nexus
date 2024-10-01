import hashlib
import random
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class Decryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

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

class SymmetricDecryption:
    def __init__(self):
        self.key = hashlib.sha256(str(random.random()).encode()).hexdigest()

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for i in range(len(encrypted_data)):
            decrypted_data += chr(ord(encrypted_data[i]) - ord(self.key[i % len(self.key)]))
        return decrypted_data

class AsymmetricDecryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

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

class HashDecryption:
    def __init__(self):
        self.hash_function = hashlib.sha256()

    def decrypt(self, encrypted_data):
        # Hash decryption is not possible, as hash functions are one-way
        return None

class BruteForceDecryption:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def decrypt(self, encrypted_data):
        for i in range(len(self.alphabet)):
            for j in range(len(self.alphabet)):
                for k in range(len(self.alphabet)):
                    key = self.alphabet[i] + self.alphabet[j] + self.alphabet[k]
                    decrypted_data = ""
                    for l in range(len(encrypted_data)):
                        decrypted_data += chr(ord(encrypted_data[l]) - ord(key[l % len(key)]))
                    if decrypted_data.isprintable():
                        return decrypted_data
        return None

class FrequencyAnalysisDecryption:
    def __init__(self):
        self.frequency = {
            'e': 12.702,
            't': 9.056,
            'a': 8.167,
            'o': 7.507,
            'i': 6.966,
            'n': 6.749,
            's': 6.327,
            'h': 6.094,
            'r': 5.987,
            'd': 4.253,
            'l': 4.025,
            'c': 2.782,
            'u': 2.758,
            'm': 2.406,
            'w': 2.309,
            'f': 2.247,
            'g': 2.015,
            'y': 1.974,
            'p': 1.929,
            'b': 1.492,
            'v': 0.978,
            'k': 0.772,
            'j': 0.153,
            'x': 0.150,
            'q': 0.095,
            'z': 0.074
        }

    def decrypt(self, encrypted_data):
        decrypted_data = ""
        for i in range(len(encrypted_data)):
            max_frequency = 0
            max_character = ""
            for j in range(len(self.frequency)):
                character = chr(ord(encrypted_data[i]) - ord(list(self.frequency.keys())[j]))
                if character.isalpha():
                    frequency = self.frequency.get(character.lower(), 0)
                    if frequency > max_frequency:
                        max_frequency = frequency
                        max_character = character
            decrypted_data += max_character
        return decrypted_data
