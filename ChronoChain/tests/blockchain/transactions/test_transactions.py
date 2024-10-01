import unittest
from blockchain.transactions import Transaction

class TestTransactions(unittest.TestCase):
    def test_transaction(self):
        transaction = Transaction("sender", "receiver", 10)
        self.assertIsNotNone(transaction.hash)

    def test_transaction_pool(self):
        transaction_pool = TransactionPool()
        transaction = Transaction("sender", "receiver", 10)
        transaction_pool.add_transaction(transaction)
        self.assertIn(transaction, transaction_pool.transactions)

    def test_transaction_processor(self):
        transaction_processor = TransactionProcessor()
        transaction = Transaction("sender", "receiver", 10)
        transaction_processor.add_transaction(transaction)
        self.assertIn(transaction, transaction_processor.transaction_pool.transactions)

    def test_transaction_validator(self):
        transaction_validator = TransactionValidator()
        transaction = Transaction("sender", "receiver", 10)
        self.assertTrue(transaction_validator.validate_transaction(transaction))

if __name__ == '__main__':
    unittest.main()
