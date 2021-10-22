# custom classes
# set up the Doubly linkedlist 
class DNode:
	def __init__(self, key, value):
		self.value = value
		self.key = key
		self.next = None
		self.prev = None

# the Doublely Linked List
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	# insert a node - at tail
	def insertNodeAtTail(self, key, value):
		node = DNode(key, value)
		# in case this is the first node
		if not self.head:
			self.head = node
			self.tail = node
			return node
		
		# add to the tail and move tail by 1 node
		self.tail.next = node
		node.prev = self.tail
		self.tail = node
		return node
	
	# insert a node - at the head
	def insertNodeAtHead(self, key, value):
		node = DNode(key, value)
		if not self.head and not self.tail:
			self.tail = node
			self.head = node
			return node
		
		# add to the head and move the head by 1 node
		self.head.prev = node
		node.next = self.head
		self.head = node
		return self.head

	# remove from tail
	def removeNodeFromTail(self):
		if self.tail is None:
			return None
		else:
			self.tail = self.tail.prev
			if self.tail is not None:
				self.tail.next = None
		
		if self.tail is not None:
			return self.tail.key


	# remove a particular node
	def removeNode(self, node):

		startNode = self.head
		while startNode and startNode.key != node.key:
			startNode = startNode.next
		
		if startNode == None:
			return None
		
		prevNode = startNode.prev
		nextNode = startNode.next

		if prevNode is not None:
			prevNode.next = nextNode
		
		if nextNode is not None:
			nextNode.prev = prevNode

		startNode = None
		
	# get the most recently used data
	def getMostRecentlyUsed(self):
		return self.head.key

	# get the least recently used data 
	def getLeastRecentlyUsed(self):
		return self.tail.key

	# print all nodes
	def printAllNodes(self):
		startNode = self.head
		while startNode:
			print(f"Node with value: {startNode.key}")
			startNode = startNode.next

	# print in reverse order
	def printReverseNodes(self):
		startNode = self.tail
		while startNode:
			print(f"Node with value: {startNode.key}")
			startNode = startNode.prev		


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
	def __init__(self, maxSize):
		self.maxSize = maxSize or 1
		self.cacheMap = {}
		self.linkedList = DoublyLinkedList()
		self.currentSize = 0

	def insertKeyValuePair(self, key, value):
		# Write your code here.
		currentBlock = self.cacheMap.get(key, None)

		print("Inserting: ", key)

		# It's a new block
		if currentBlock == None:
			if self.currentSize < self.maxSize:
				self.cacheMap[key] = self.linkedList.insertNodeAtHead(key, value)
				self.currentSize += 1
			else:
				# evict the least recently used - the item at the tail
				nodeRemovedKey = self.linkedList.removeNodeFromTail()
				print(f"Removed Node: {nodeRemovedKey}")
				
				# free the slot in cacheMap
				if nodeRemovedKey is not None:
					self.cacheMap[nodeRemovedKey] = None
					self.cacheMap.pop(nodeRemovedKey)
					
				# assign the block to the new data
				newBlock = self.linkedList.insertNodeAtHead(key, value)
				self.cacheMap[newBlock.key] = newBlock

		# it's an existing block 
		else:
			# make the node head since it's the most recently used now
			newNode = self.linkedList.insertNodeAtHead(key, value)
			self.cacheMap[newNode.key] = newNode
			self.linkedList.removeNode(currentBlock)


	def getValueFromKey(self, key):
		currentBlock = self.cacheMap.get(key, None)

		if currentBlock == None:
			return None
		else:
			# make this block the most recently accessed
			newNode = self.linkedList.insertNodeAtHead(key, currentBlock.value)
			self.cacheMap[key] = newNode
			self.linkedList.removeNode(currentBlock)

			return newNode.value

	def getMostRecentKey(self):
		return self.linkedList.getMostRecentlyUsed()





# -------------------- TEST ------------------------------
def test_algoexpert_lru():
	lruCache = LRUCache(1)


	print(lruCache.getValueFromKey("a"))
	lruCache.insertKeyValuePair("a", 1)

	# print(lruCache.getValueFromKey("a"))

	lruCache.insertKeyValuePair("a",9001)

	print(lruCache.cacheMap.keys())

	# print(lruCache.getValueFromKey("a"))
	
	lruCache.insertKeyValuePair("b", 2)

	# print(lruCache.getValueFromKey("a"))

	# print(lruCache.getValueFromKey("b"))

	lruCache.insertKeyValuePair("c", 3)

	print(lruCache.cacheMap.keys())



	# print(lruCache.getValueFromKey("a"))

	# print(lruCache.getValueFromKey("b"))



test_algoexpert_lru()