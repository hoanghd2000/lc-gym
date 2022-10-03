from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack: Always about, when do you need to pop from the stack?
        
        operators = set(['+', '-', '*', '/'])
        stack = []
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand1 = stack.pop()
                operand0 = stack.pop()
                if token == '+':
                    stack.append(operand0 + operand1)
                elif token == '-':
                    stack.append(operand0 - operand1)
                elif token == '*':
                    stack.append(operand0 * operand1)
                else:
                    stack.append(int(operand0 / operand1))
            #print(stack)
        
        return stack[0]