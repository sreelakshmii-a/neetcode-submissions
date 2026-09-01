class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x == '+':
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append(val2 + val1)
            elif x == '-':
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append(val2 - val1)
            elif x == '*':
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append(val2 * val1)
            elif x == '/':
                val1=int(stack.pop())
                val2=int(stack.pop())
                stack.append(int(val2/val1))
            else:
                stack.append(x)
                
        return int(stack[-1])