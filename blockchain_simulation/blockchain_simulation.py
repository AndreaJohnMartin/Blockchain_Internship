# blockchain.py
import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_content = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(block_content.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "hash": self.hash,
            "nonce": self.nonce
        }

def create_blockchain():
    chain = []
    genesis_block = Block(0, time.time(), "Genesis Block", "0")
    chain.append(genesis_block)

    for i in range(1, 3):
        new_block = Block(i, time.time(), f"Block {i} Data", chain[-1].hash)
        chain.append(new_block)
    return chain

def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i - 1]
        if current.previous_hash != previous.hash:
            return False
        if current.hash != current.generate_hash():
            return False
    return True
