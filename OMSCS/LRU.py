from DoublyLinkedList import *

class LRUCache: 
	def __init__(self, cacheSize):
		self.currentSize = 0
		self.cacheSize = cacheSize
		self.cacheMap = {}
		self.linkedList = DoublyLinkedList()

	# insert a block into the cache
	def insertData(self, data)
		# check if the block is in the cacheMap
			# if yes: get the node and update the linkedList
			# else: 
				# if currentSize < cacheSize: get a free slot in cacheMap and update the linkedList
				# else: evict the least recently used block from cacheMap and update the linkedList
		currentBlock = cacheMap.get(data, None)
		
		# It's a new block
		if currentBlock == None:
			if self.currentSize < self.cacheSize:
				self.cacheMap[data] = self.linkedList.insertNodeAtHead(data)
				self.currentSize += 1
			else:
				# evict the least recently used - the item at the tail
				nodeRemoved = self.linkedList.removeNodeFromTail()
				print(f"Removed Node with value: {nodeRemoved.value}")
				# free the slot in cacheMap
				self.cacheMap[nodeRemoved.value] = None
				
				# assign the block to the new data
				newBlock = self.linkedList.insertNodeAtHead(data)
				self.cacheMap[newBlock.value] = newBlock

		# it's an existing block 
		else:
			# make the node head since it's the most recently used now
			newNode = self.linkedList.insertNodeAtHead(currentBlock.value)
			self.cacheMap[newBlock.value] = newNode
			self.removeNode(currentBlock)


	# get a block from the cache
	def getData(self, data):
		if self.cacheMap[data]:
			return self.cacheMap[data].value
		print(f"Not data found for: {data}")
		return None

	# print current cache items
	def printCache(self):
		for block in cacheMap:
			print(f"Block: {block.value}")

