def sortedInsert(head, data):
    newNode = DoublyLinkedListNode(data)
    newNode.data = data

    if head is None:
        return newNode

    current = head
    while current.next is not None and current.data < newNode.data and current.next.data < newNode.data:
        current = current.next

    if current.next is None:
        current.next = newNode
        newNode.prev = current
        return head
    
    if current == head:
        newNode.next = current
        current.prev = newNode
        return newNode

    
    temp = current.next
    current.next = newNode
    newNode.prev = current
    newNode.next = temp
    temp.prev = newNode

    return head