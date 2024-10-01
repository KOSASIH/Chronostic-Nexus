import unittest
from blockchain.consensus import Consensus

class TestConsensus(unittest.TestCase):
    def test_proof_of_work(self):
        consensus = Consensus()
        block = Block(1, "0", int(time.time()), [])
        consensus.proof_of_work(block)
        self.assertIsNotNone(block.hash)

    def test_mine_block(self):
        consensus = Consensus()
        block = Block(1, "0", int(time.time()), [])
        consensus.mine_block(block)
        self.assertIsNotNone(block.hash)

    def test_validate_block(self):
        consensus = Consensus()
        block = Block(1, "0", int(time.time()), [])
        consensus.validate_block(block)
        self.assertTrue(block.hash == block.calculate_hash())

    def test_resolve_conflicts(self):
        consensus = Consensus()
        block = Block(1, "0", int(time.time()), [])
        consensus.resolve_conflicts()
        self.assertIsNotNone(block.hash)

if __name__ == '__main__':
    unittest.main()
