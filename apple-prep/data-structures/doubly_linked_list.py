class Node:
	def __init__(self, value = 0, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
	
class DoublyLinkedList:
	def __init__(self, totalNumberOfNodes = 0):
		self.head = None
		self.tail = None
		self.totalNumberOfNodes = 0

	# insert a node at the head 
	def insert_head(self, value):
		node = Node(value)
		self.totalNumberOfNodes += 1
		# if head is None then it's the first node
		if self.head is None:
			self.head = node
			self.tail = node
			return node

		self.head.prev = node
		node.next = self.head
		self.head = node
		self.head.prev = None
		return node
	
	# insert a node in the tail
	def insert_tail(self, value):
		node = Node(value)
		self.totalNumberOfNodes += 1
		if self.tail is None:
			self.tail = node
			self.head = node
			return
		
		self.tail.next = node
		node.prev = self.tail
		self.tail = node

	# remove node from the head
	def remove_node_at_head(self):
		if self.totalNumberOfNodes == 1:
			remove_node = self.head
			self.head = None
			self.tail = None
			self.totalNumberOfNodes -= 1
			return remove_node
		
		elif self.totalNumberOfNodes == 0:
			print("No node to remove!")
			return None

		removed_node = self.head
		self.head = self.head.next
		self.head.prev = None
		self.totalNumberOfNodes -= 1
		return removed_node
	
	# remove node from the tail
	def remove_node_at_tail(self):
		if self.totalNumberOfNodes == 1:
			self.head = None
			self.tail = None
			self.totalNumberOfNodes -= 1
			return
		elif self.totalNumberOfNodes == 0:
			print("No node to remove!")
			return
		
		self.tail = self.tail.prev
		self.tail.next = None
		self.totalNumberOfNodes -= 1

	# search for a node
	def search(self, target_value):
		if self.totalNumberOfNodes == 0:
			print("No node is there!")
			return
		
		current_pos = 0
		current_node = self.head
		while current_node:
			if current_node.value == target_value:
				return (current_node.value, current_pos)
			
			current_node = current_node.next
			current_pos += 1

		return (None, None)