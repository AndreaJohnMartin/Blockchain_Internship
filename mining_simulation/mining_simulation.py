# mining_simulation.py
import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash='0'):
        self.index = index
        self.timestamp = time.time()
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

    def mine_block(self, difficulty):
        prefix = '0' * difficulty
        start_time = time.time()

        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.generate_hash()

        end_time = time.time()
        print(f"Block mined with nonce: {self.nonce}")
        print(f"Hash: {self.hash}")
        print(f"Time taken: {end_time - start_time:.4f} seconds")

# Example usage
if __name__ == "__main__":
    difficulty = 4  # You can increase this to make mining harder
    block = Block(1, "Test block", "0")
    block.mine_block(difficulty)
