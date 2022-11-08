from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                nxt = [1]
                for j in range(i-1):
                    nxt.append(res[-1][j] + res[-1][j+1])
                nxt.append(1)
                res.append(nxt)
        return res