from __future__ import print_function

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
	# loop till we find the start point p
	while head.next.value != p:
		head = head.next

	# loop and find the end point
	tail = head
	while tail.value != q:
		tail = tail.next
	
	# reverse the cycle
	prev = None
	current = head.next
	start = head.next
	resume = tail.next

	while current != None:
		next = current.next
		current.next = prev
		if current == tail:
			break
		prev = current
		current = next

	start.next = resume
	head.next = tail
	
	return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
