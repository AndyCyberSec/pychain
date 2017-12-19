import hashlib
import time
import json


class Block(object):

    def __init__(self, difficulty, index, data, previous_hash=''):
        self.difficulty = difficulty
        self.nonce = 0

        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = time.time()
        self.hash = self.hash_calculation()

    def hash_calculation(self):

        return hashlib.sha256(str(self.index).encode() + str(self.data).encode() + str(self.timestamp).encode() +
                              str(self.nonce).encode()).hexdigest()

    def block_mining(self):

        while self.hash[0:self.difficulty] != "0" * self.difficulty:
            self.nonce += 1
            self.hash = self.hash_calculation()

        # print ("Block mined:" + self.hash + " nonce:" + str(self.nonce))#


class BlockChain(object):

    def __init__(self, difficulty):
        self.chain = [self.genesis_block]
        self.difficulty = difficulty

    @staticmethod
    def genesis_block(self):
        return Block(2, 0, "GENESIS", "xxx")

    @staticmethod
    def get_prev_block(self):
        block = self.chain[len(self.chain)-1]
        return block.hash

    def add_block(self, new_block):

        new_block.previous_hash = self.get_prev_block
        new_block.block_mining()
        self.chain.append(new_block)

    @property
    def chain_validation(self):

        for k, block in enumerate(self.chain):

            if k > 0:
                print(dir(block))
                prev_block = self.chain[k-1]
                if block.hash != block.hash_calculation:
                    return False
                if block.previous_hash != prev_block.hash:
                    return False

            else:

                pass
        return True


diff = 3

data1 = json.dumps({'username': 'Pippo', 'amount': 1.00}, sort_keys=True, indent=4)
data2 = json.dumps({'username': 'Baudo', 'amount': 5.00}, sort_keys=True, indent=4)
data3 = json.dumps({'username': 'Pippo', 'amount': 1.00}, sort_keys=True, indent=4)
data4 = json.dumps({'username': 'Pippo', 'amount': 1.00}, sort_keys=True, indent=4)

b = BlockChain(diff)
b.add_block(Block(diff, 1, data1))
b.add_block(Block(diff, 2, data2))
b.add_block(Block(diff, 3, data3))
# b.chain[1].hash = "fega" #PoW
b.add_block(Block(diff, 4, data4))
print("Chain is valid?: " + str(b.chain_validation))

for elements in b.chain:
    print("data: " + elements.data + " hash: " + elements.hash)
