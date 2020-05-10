from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        input_list = convertLinkedListToList(head)
        
        # ds
        stack = []
        output_list = []
        o_i = 0

        # loop over all elements of the input_list
        for i in range(len(input_list)):
            item = input_list[i]
            if len(stack) == 0:
                stack.append(item)
            else:
                while item > stack[len(stack)-1]:
                    if input_list[o_i] < item:
                        output_list.append(item)
                        o_i += 1
                        stack.pop()
                    if len(stack) == 0:
                        break
                # insert and sort
                stack = sortAndInsertStack(stack, item)

        # check if stack is not empty
        print(input_list)
        print(output_list)
        print(stack)
        print(o_i)
        while len(stack):
            item = stack[len(stack) - 1]
            if len(output_list) == len(input_list) - 1:
                output_list.append(0)
                break
            while o_i < len(input_list) and item > input_list[o_i]:
                output_list.append(item)
                o_i += 1

            if len(output_list) == len(input_list):
                break
            output_list.append(0)
            o_i += 1
            stack.pop()

        # print(output_list)
        return output_list


def sortAndInsertStack(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return stack
    
    if element == 0:
        stack.insert(0, element)
        return stack
    
    top = len(stack) - 1
    while element < stack[top]:
        top -= 1
        if top < 0:
            break

    stack.insert(top+1, element)
    return stack 


def convertLinkedListToList(ll):
    temp = ll
    res = []
    while temp != None:
        res.append(temp.val)
        temp = temp.next

    return res


# node = ListNode(2)
# node.next = ListNode(1)
# node.next.next = ListNode(5)

# x = Solution()
# x.nextLargerNodes(node)


# node = ListNode(2)
# node.next = ListNode(7)
# node.next.next = ListNode(4)

# x = Solution()
# x.nextLargerNodes(node)

# node = ListNode(5)
# node.next = ListNode(2)
# node.next.next = ListNode(5)

# x = Solution()
# x.nextLargerNodes(node)


# node = ListNode(2)
# node.next = ListNode(7)
# node.next.next = ListNode(4)
# node.next.next.next = ListNode(3)
# node.next.next.next.next = ListNode(5)

# x = Solution()
# x.nextLargerNodes(node)

# [1,7,5,1,9,2,5,1]
# node = ListNode(1)
# node.next = ListNode(7)
# node.next.next = ListNode(5)
# node.next.next.next = ListNode(1)
# node.next.next.next.next = ListNode(9)
# node.next.next.next.next.next = ListNode(2)
# node.next.next.next.next.next.next = ListNode(5)
# node.next.next.next.next.next.next.next = ListNode(1)

# x = Solution()
# x.nextLargerNodes(node)

# [1,7,5,1,9,2,5,1]

# node = ListNode(1)
# node.next = ListNode(7)
# node.next.next = ListNode(5)
# node.next.next.next = ListNode(1)
# node.next.next.next.next = ListNode(9)
# node.next.next.next.next.next = ListNode(2)
# node.next.next.next.next.next.next = ListNode(5)
# node.next.next.next.next.next.next.next = ListNode(1)

# x = Solution()
# x.nextLargerNodes(node)


# [10,4,6,4,10]
node = ListNode(10)
node.next = ListNode(4)
node.next.next = ListNode(6)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(10)

x = Solution()
print(x.nextLargerNodes(node))



