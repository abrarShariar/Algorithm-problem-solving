# SOLVED
import operator
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for ch in tokens:
            if ch in ops.keys():
                # operator
                op2 = stack.pop()
                op1 = stack.pop()
                op_func = ops[ch]
                result = int(op_func(op1, op2))
                stack.append(result)
            else:
                # integer
                stack.append(int(ch))
        
        return stack.pop()

x = Solution()
x.evalRPN(["2", "1", "+", "3", "*"])
x.evalRPN(["4", "13", "5", "/", "+"])
print(x.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


