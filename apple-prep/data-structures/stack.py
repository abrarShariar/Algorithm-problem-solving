from doubly_linked_list import DoublyLinkedList

class Stack:
	def __init__(self, stack_size = 0):
		self.stack_size = stack_size
		self.element_list = DoublyLinkedList(self.stack_size)

	# push on top of stack
	def push(self, value):
		node = self.element_list.insert_head(value)
		self.stack_size += 1
		print("Push: ", node.value)
	
	# pop from the top of stack
	def pop(self):
		if self.stack_size == 0:
			print("Stack is empty")
			return
		
		node = self.element_list.remove_node_at_head()
		self.stack_size -= 1
		print("Pop: ", node.value)

	# peek at the top of the stack
	def peek(self):
		if self.stack_size == 0:
			print("Stack is empty")
			return
		
		return self.element_list.head.value
	
	# search for an element
	def search(self, value):
		if self.stack_size == 0:
			print("Stack is empty!")
			return

		(result_value, result_index) = self.element_list.search(value)
		if result_index is not None and result_value is not None:
			print("Found {} in index {}".format(result_value, result_index))
		else:
			print("NOT FOUND!")

	
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)


stack.pop()

stack.search(3)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
