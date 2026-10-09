class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {
            '+':lambda op1, op2:op1 + op2,
            '-':lambda op1, op2:op1 - op2,
            '*':lambda op1, op2:op1 * op2,
            '/':lambda op1, op2:int(op1/op2)
        }
        for i in tokens:
            if i in ops:
                op2=stack.pop()
                op1=stack.pop()
                stack.append(ops[i](op1, op2))
            else:
                stack.append(int(i))
        return stack[0]
