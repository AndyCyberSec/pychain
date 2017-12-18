import hashlib
import time
import json

class Block:

	def __init__(self, difficulty, index, data, previousHash=''):

		self.difficulty = difficulty
		self.nonce = 0

		self.index = index 
		self.previousHash = previousHash 
		self.data = data
		self.timestamp = time.time()
		self.hash = self.hashCalculation()
		
	#builds the current block hash
	def hashCalculation(self):

		return hashlib.sha256(str(self.index).encode() + str(self.data).encode() + str(self.timestamp).encode() + str(self.nonce).encode()).hexdigest()

	#mine the block
	def blockMining(self):

		#check if the firsts n(difficulty) characters of the hash containing n(difficulty) zeroes
		#if so, loop exits and we have hash that begins with n(dofficulty) zeroes
		while(self.hash[0:self.difficulty] != ("0" * self.difficulty)):

			self.nonce += 1
			self.hash = self.hashCalculation()

		#print ("Block mined:" + self.hash + " nonce:" + str(self.nonce))



class BlockChain():

	def __init__(self, difficulty):

		self.chain = [self.genesisBlock()]
		self.difficulty = difficulty

	def genesisBlock(self):

		self.genesis = Block(2, 0, "GENESIS", "passphrase")
		return self.genesis

	def getPrevBlock(self):

		self.lastBlock = self.chain[len(self.chain)-1]
		return self.lastBlock

	def addBlock(self, newBlock):

		self.newBlock = newBlock
		self.newBlock.previousHash = self.getPrevBlock().hash;
		self.newBlock.blockMining()
		self.chain.append(self.newBlock)

	def chainValidation(self):

		for k, block in enumerate(self.chain):

			if k > 0: #skip the genesis block who has not previous hash

				prevBlock = self.chain[k-1]
				curBlock = block

				if curBlock.hash != curBlock.hashCalculation():
					return False
				if curBlock.previousHash != prevBlock.hash:
					return False

			else:

				pass

		return True


difficulty = 3

data1 = json.dumps({'username':'Pippo', 'amount':1.00}, sort_keys=True, indent=4)
data2 = json.dumps({'username':'Baudo', 'amount':5.00}, sort_keys=True, indent=4)
data3 = json.dumps({'username':'Pippo', 'amount':1.00}, sort_keys=True, indent=4)
data4 = json.dumps({'username':'Pippo', 'amount':1.00}, sort_keys=True, indent=4)


print(data1)

b = BlockChain(difficulty)
b.addBlock(Block(difficulty, 1, data1))
b.addBlock(Block(difficulty, 2, data2))
b.addBlock(Block(difficulty, 3, data3))
#b.chain[1].hash = "fega" #PoW
b.addBlock(Block(difficulty, 4, data4))
print("Chain is valid?: " + str(b.chainValidation()))

for elements in b.chain:
	print("data: " + elements.data + " hash: " + elements.hash)