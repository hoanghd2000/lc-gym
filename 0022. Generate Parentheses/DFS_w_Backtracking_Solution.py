from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if openN < n
        # only add a closing parenthesis if closingN < openN
        # with the above 2 rules, valid IIF openN == closingN == n
        
        stack = []
        res = []
        
        def dfs_backtrack(openN, closingN):
            if openN == closingN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                dfs_backtrack(openN + 1, closingN)
                stack.pop()
            
            if closingN < openN:
                stack.append(')')
                dfs_backtrack(openN, closingN + 1)
                stack.pop()
        
        dfs_backtrack(0,0)
        
        return res