import hashlib
import time
from transaction import Transaction

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.nodes = []

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner):
        if not self.pending_transactions:
            return False

        new_block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.sender) + str(self.receiver) + str(self.amount) + str(self.timestamp)
        return hashlib.sha256(data.encode()).hexdigest()

class Node:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def send_message(self, message):
        for connection in self.connections:
            connection.send(message)

class Connection:
    def __init__(self, node):
        self.node = node

    def send(self, message):
        self.node.blockchain.add_transaction(message)

class Message:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.sender) + str(self.receiver) + str(self.amount) + str(self.timestamp)
        return hashlib.sha256(data.encode()).hexdigest()
