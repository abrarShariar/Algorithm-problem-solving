
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0

    def print(self):
        if self.is_empty():
            raise Exception("The stack is empty")

        return " ".join([str(item) for item in self.stack])

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print(stack.print())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())

def isBalanced(input_str):
    stack = Stack()
    closing_brackets = {')', '}', ']'}
    matching_brackets = {
        ')': '(',
        '}': '{',
        ']': '[' 
    }

    opening_brackets = matching_brackets.keys()

    for ch in input_str:
        if ch in opening_brackets:
            stack.push(ch)
        elif ch in closing_brackets:
            if stack.is_empty():
                return False
            popped_item = stack.pop()
            if not matching_brackets[ch] == popped_item:
                return False
    
    return stack.is_empty()