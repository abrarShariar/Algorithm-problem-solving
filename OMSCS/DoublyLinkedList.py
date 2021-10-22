# set up the Doubly linkedlist 
class DNode:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

# the Doublely Linked List
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	# insert a node - at tail
	def insertNodeAtTail(self, value):
		node = DNode(value)
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
	def insertNodeAtHead(self, value):
		node = DNode(value)
		if not self.tail:
			self.tail = node
			self.head = node
			return node
		
		# add to the head and move the head by 1 node
		self.head.prev = node
		node.next = self.head
		self.head = node
		return node

	# remove from tail
	def removeNodeFromTail(self):
		nodeToRemove = self.tail
		prevNode= self.tail.prev
		nodeToRemove.prev = None
		self.tail = prevNode
		self.tail.next = None
		return nodeToRemove

	# remove a particular node
	def removeNode(self, node):
		# update the node's pointers and remove it
		prevNode = node.prev
		nextNode = node.next
		prevNode.next = nextNode
		nextNode.prev = prevNode
		node.value = None

	# get the most recently used data
	def getMostRecentlyUsed(self):
		return self.head.value

	# get the least recently used data 
	def getLeastRecentlyUsed(self):
		return self.tail.value

	# print all nodes
	def printAllNodes(self):
		startNode = self.head
		while startNode:
			print(f"Node with value: {startNode.value}")
			startNode = startNode.next

	# print in reverse order
	def printReverseNodes(self):
		startNode = self.tail
		while startNode:
			print(f"Node with value: {startNode.value}")
			startNode = startNode.prev		


