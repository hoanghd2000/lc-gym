from typing import List

class Solution:
    def generate(self, n: int) -> List[str]:
        # base case
        if n == 0:
            return ['']
        
        # recursive step
        substrs = self.generate(n-1)
        res = []
        for substr in substrs:
            res.append('()'+substr)
            res.append('(('+substr)
            res.append(')('+substr)
            res.append('))'+substr)
        return res
        
    def generateParenthesis(self, n: int) -> List[str]:
        strs = self.generate(n)
        res = []
        for str in strs:
            bal = 0
            found = True
            for char in str:
                if char == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    found = False
                    break
            if found and not bal:
                res.append(str)
        return res