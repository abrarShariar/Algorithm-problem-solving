class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(20)
queue.enqueue(300)

print(queue.is_empty())

while not queue.is_empty():
    print(queue.dequeue())

print(queue.is_empty())
