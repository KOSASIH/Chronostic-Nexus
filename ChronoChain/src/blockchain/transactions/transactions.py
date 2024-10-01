import hashlib
import time
from blockchain import Blockchain

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

class TransactionPool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def clear_transactions(self):
        self.transactions = []

class TransactionProcessor:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.transaction_pool = TransactionPool()

    def add_transaction(self, transaction):
        self.transaction_pool.add_transaction(transaction)

    def process_transactions(self):
        transactions = self.transaction_pool.get_transactions()
        for transaction in transactions:
            self.blockchain.add_transaction(transaction)
        self.transaction_pool.clear_transactions()

class TransactionValidator:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def validate_transaction(self, transaction):
        if transaction.sender != self.blockchain.get_latest_block().hash:
            return False
        if transaction.receiver != self.blockchain.get_latest_block().hash:
            return False
        if transaction.amount <= 0:
            return False
        return True

class TransactionMiner:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine_transactions(self):
        transactions = self.blockchain.pending_transactions
        for transaction in transactions:
            self.blockchain.add_block(transaction)
        self.blockchain.pending_transactions = []
