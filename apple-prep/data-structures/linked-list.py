# the node class
class Node:
	def __init__(self, value = 0, next = None):
		self.value = value
		self.next = next

# the singly linked-list class
class SinLinkedList:	
	def __init__(self, totalNumberOfNodes = 0, head = None, tail = None):
		self.totalNumberOfNodes = totalNumberOfNodes
		self.head = None
		self.tail = None
	
	# insert at the head of the linkedList
	def insert_head(self, value):
		# create a new node with the value to insert
		node = Node(value)

		# if head is None - it is the first node in the linked list
		if self.head is None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
		
		# if tail is None - head and tail now points to the same node
		if self.tail is None:
			self.tail = node
		
		self.totalNumberOfNodes += 1
	
	def insert_tail(self, value):
		# create a new node with the value to insert
		node = Node(value)

		# if tail is None then it is the first tail node
		if self.tail is None:
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		
		# if head is None - the head and tail are the same Node
		if self.head is None:
			self.head = node
		
		self.totalNumberOfNodes += 1

	# insert node at position [0...N]
	def insert_node(self, value, position):

		if position >= self.totalNumberOfNodes:
			print("The position you entered is out of range")
			return
		elif position == 0:
			self.insert_head(value)
			return
		elif position == self.totalNumberOfNodes - 1:
			self.insert_tail(value)
			return 

		current_node = self.head
		current_pos = 0
		# we loop over till the current_node is pointing to 1 node before our target position
		while current_pos < position - 1:
			current_node = current_node.next
			current_pos += 1
		
		new_node = Node(value)
		new_node.next = current_node.next
		current_node.next = new_node

		self.totalNumberOfNodes += 1
		return new_node


	def print_all_nodes(self):
		start_node = Node()
		start_node = self.head
		node_index = 0

		print("Total number of nodes: ", self.totalNumberOfNodes)

		# while start_node is not null
		while start_node:
			print("Node at index : ", node_index, " value: ", start_node.value)
			start_node = start_node.next
			node_index += 1
		
		print("Finished printing all nodes")



ll = SinLinkedList()
ll.insert_head(0)
ll.insert_tail(1)
ll.insert_head(10)
ll.insert_node(99, 1)
ll.insert_node(99999, 100)
ll.insert_node(55, 0)

ll.insert_node(55, ll.totalNumberOfNodes - 1)

ll.print_all_nodes()



