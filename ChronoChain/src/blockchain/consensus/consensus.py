import hashlib
import time
from blockchain import Blockchain

class Consensus:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def proof_of_work(self, block):
        new_hash = block.calculate_hash()
        while not new_hash.startswith('0' * self.blockchain.difficulty):
            block.nonce += 1
            new_hash = block.calculate_hash()
        return new_hash

    def mine_block(self, block):
        self.proof_of_work(block)

    def validate_block(self, block):
        if block.hash != block.calculate_hash():
            return False
        if block.previous_hash != self.blockchain.get_latest_block().hash:
            return False
        return True

    def resolve_conflicts(self):
        longest_chain = self.blockchain.chain
        for node in self.blockchain.nodes:
            if len(node.chain) > len(longest_chain):
                longest_chain = node.chain
        self.blockchain.chain = longest_chain
        return True

class ProofOfWork(Consensus):
    def __init__(self, blockchain):
        super().__init__(blockchain)

    def proof_of_work(self, block):
        new_hash = block.calculate_hash()
        while not new_hash.startswith('0' * self.blockchain.difficulty):
            block.nonce += 1
            new_hash = block.calculate_hash()
        return new_hash

class ProofOfStake(Consensus):
    def __init__(self, blockchain):
        super().__init__(blockchain)

    def proof_of_stake(self, block):
        validators = self.blockchain.validators
        validator = np.random.choice(validators)
        return validator

class DelegatedProofOfStake(Consensus):
    def __init__(self, blockchain):
        super().__init__(blockchain)

    def delegated_proof_of_stake(self, block):
        validators = self.blockchain.validators
        validator = np.random.choice(validators)
        return validator

class ByzantineFaultTolerance(Consensus):
    def __init__(self, blockchain):
        super().__init__(blockchain)

    def byzantine_fault_tolerance(self, block):
        validators = self.blockchain.validators
        validator = np.random.choice(validators)
        return validator
