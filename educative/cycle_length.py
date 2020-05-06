class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_cycle_length(head):
	tort, hare = head, head.next
	while hare.value != tort.value:
		hare = hare.next.next
		tort = tort.next

	if hare.value == tort.value:
		return calculate_cycle_length(tort)
	else:
		return 0

def calculate_cycle_length(slow):
	start = slow
	end = start.next
	length = 1
	while start.value != end.value:
		length += 1
		end = end.next

	return length


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
