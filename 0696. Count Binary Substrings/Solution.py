class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        curchar = s[0]
        countList = []
        res = 0
        
        for i in range(1, len(s)):
            if s[i] != curchar:
                countList.append(count)
                curchar = s[i]
                count = 1
            else:
                count += 1
            
            if i == len(s)-1:
                countList.append(count)
            
        for i in range(len(countList)-1):
            res += min(countList[i], countList[i+1])
        
        return res